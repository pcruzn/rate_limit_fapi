# we are in the routers file
from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler


limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix="/users")
router.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
