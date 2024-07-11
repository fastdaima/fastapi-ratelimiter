# FastAPI Ratelimiter

- This is a custom package version, for anyone who want to clone it as module and using it in their project
- To use this version, just do an git clone, and use this fastapi_ratelimiter module
- This version is on par with redis recent version 
- For original implementation as a package visit: [fastapi_ratelimiter](https://github.com/GLEF1X/fastapi-ratelimiter)


# New Features: 
- Yet to be announced. Stay tuned!

## Quick start:

```python
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
```