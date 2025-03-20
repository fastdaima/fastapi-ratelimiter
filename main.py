from redis.asyncio import Redis

import uvicorn
from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse
import asyncio

from fastapi_ratelimiter.depends import RateLimited, RedisDependencyMarker
from fastapi_ratelimiter.strategies import BucketingRateLimitStrategy

app = FastAPI()
redis = Redis.from_url("redis://localhost:6379")


@app.get(
    "/some_expensive_call", response_class=JSONResponse,
    dependencies=[
        Depends(RateLimited(BucketingRateLimitStrategy(rate="1/60s")))
    ]
)
async def handle_test_endpoint():
    await asyncio.sleep(5)
    return {"hello": "world"}


app.dependency_overrides[RedisDependencyMarker] = lambda: redis

if __name__ == '__main__':
    uvicorn.run(app)
