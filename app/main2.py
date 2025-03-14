from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from app.routers.users2 import router as users_router
app = FastAPI()
app.include_router(users_router)

# this defines a max; if a router sets a limit less than this one, then
# the router limit prevails. if a router sets a limit higher than this one,
# the default prevails.
limiter = Limiter(key_func=get_remote_address, default_limits=["5/minute"])


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
@app.get("/")
def root(request: Request):
    print(request.method)
    return {"message": "Hello World"}