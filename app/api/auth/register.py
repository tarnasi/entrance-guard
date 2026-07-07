from fastapi import APIRouter, HTTPException
import bcrypt
from binascii import Error as BinasciiError

from app.db.mysql import db
from app.utils.rsa import decrypt_password

router = APIRouter()


@router.post("/register")
async def register(data: dict):
    try:
        password = decrypt_password(data["password"])
    except (BinasciiError, ValueError):
        raise HTTPException(status_code=400, detail="Invalid encrypted password")

    cursor = db.cursor(dictionary=True)
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt(),
    )
    
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
        (data["name"], data["email"], hashed)
    )
    
    db.commit()
    return {"message": "User registred successfully"}


