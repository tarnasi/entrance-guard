import time

from jose import jwt

from app.config import get_settings

settings = get_settings()

def sign_token(user):
    payload = {
        "id": user['id'],
        "email": user["email"],
        "exp": time.time() + int(settings.JWT_EXPIRES)
    }
    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=['RSA256']
    )


def verify_token(token):
    return jwt.decode(
        token,
        settings.JWT_SECRET,
        algorithms=["RSA256"]
    )
