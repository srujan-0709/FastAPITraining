from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["college"]

# Select collection
students_collection = db["student"]

@app.get("/")
async def home():
    return {
        "message": "FastAPI with MongoDB is working"
    }

@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mongodb":"Connected", "ping": result["ok"]}