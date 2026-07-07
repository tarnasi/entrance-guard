from fastapi import FastAPI

from app.api.auth import login, logout, profile, register


app = FastAPI(
    title="Base Service Authentication and Authorization"
)

app.include_router(register.router, prefix="/api/auth")
app.include_router(login.router, prefix="/api/auth")
app.include_router(profile.router, prefix="/api/auth")
app.include_router(logout.router, prefix="/api/auth")

@app.get('/')
def main_page():
    return {
        "prefix": "api/auth",
        "title": "enterance",
        "owner": "shahriyar tarnasi",
        "contactMe": "shahryar.tarnasi@gmail.com"
    }
