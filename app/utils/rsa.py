from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64


with open("storage/rsa/private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

with open("storage/rsa/public.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())


def encrypt_password(plain: str) -> str:
    encrypted = public_key.encrypt(
        plain.encode(),
        padding.PKCS1v15(),
    )
    return base64.b64encode(encrypted).decode()


def decrypt_password(encrypted: str) -> str:
    decrypted = private_key.decrypt(
        base64.b64decode(encrypted),
        padding.PKCS1v15(),
    )
    return decrypted.decode()



