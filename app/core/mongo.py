from pymongo import MongoClient
from gridfs import GridFS
from app.config import settings

client = MongoClient(
    settings.MONGODB_URI,
    maxPoolSize=settings.MONGODB_MAX_POOL_SIZE,
    minPoolSize=settings.MONGODB_MIN_POOL_SIZE,
)

db = client[settings.MONGODB_DB_NAME]
fs = GridFS(db)
