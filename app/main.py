from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
from app.routers.users import router as users_router
app = FastAPI()
app.include_router(users_router)

#replaces _rate_limit_exceeded_handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_exception_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Too many requests, try again later.",
            "reason": str(exc)
        }
    )

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exception_handler)
@app.get("/")
@limiter.limit("5/minute")
def root(request: Request):
    print(request.method)
    return {
        "message": "Hello World"
    }