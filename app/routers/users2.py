from fastapi import APIRouter, Request


router = APIRouter(prefix="/users")

@router.get("/")
def get_users(request: Request):
    return [
        {
            "username": "admin",
            "email": "admin@localhost",
        },
        {
            "username": "user",
            "email": "user@localhost",
        }
    ]