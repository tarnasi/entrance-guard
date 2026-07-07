from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
async def logout():
    return {"message": "Logout handled on client side"}
