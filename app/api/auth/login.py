from fastapi import APIRouter, HTTPException
import bcrypt
from binascii import Error as BinasciiError

from app.utils.jwt import sign_token
from app.utils.rsa import decrypt_password
from app.db.mysql import db
from app.config import get_settings

router = APIRouter()

settings = get_settings()


@router.post("/login")
def login(data: dict):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (data["email"],))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    try:
        password = decrypt_password(data["password"])
    except (BinasciiError, ValueError):
        raise HTTPException(status_code=400, detail="Invalid encrypted password")

    if not bcrypt.checkpw(password.encode(), user["password"].encode()):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return {
        "user": {
            "id": user['id'],
            "name": user['name'],
            "email": user['email'],
        },
        "access_token": sign_token(user),
        "expire_times": settings.JWT_EXPIRES,
        "token_type": "Bearer"
    }
