from fastapi import FastAPI
from redis.asyncio import Redis
import os

app = FastAPI()

# Setup Redis connection
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", "6379")
redis = None

@app.on_event("startup")
async def startup_event():
    global redis
    redis = Redis(host=redis_host, port=int(redis_port))

@app.on_event("shutdown")
async def shutdown_event():
    await redis.close()

@app.get("/")
async def read_root():
    # Example Redis command
    await redis.set("mykey", "Hello from Redis!")
    value = await redis.get("mykey", encoding="utf-8")
    return {"message": value}

@app.get("/redis")
async def test_redis_connection():
    try:
        pong = await redis.ping()
        if pong:
            return {"status": "Connection to Redis is successful"}
        else:
            return {"status": "Connection to Redis failed"}
    except Exception as e:
        return {"status": f"error: {str(e)}"}

@app.get("/up")
async def health_check():
    '''
    Health check endpoint to ensure the container is running
    '''
    return {"status": "OK"}
