from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix="/users")

# the limit is set per router
@router.get("/")
@limiter.limit("2/minute")
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
