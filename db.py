import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


load_dotenv()

try:
    MONGO_URI = os.getenv("MONGO_URI")

    if not MONGO_URI:
        raise ValueError("MONGO_URI not foung in .env file")

    
    client = MongoClient(MONGO_URI)

    
    db = client["cats_db"]
    collection = db["cats"]

    
    if collection.count_documents({}) == 0: 
        collection.insert_one({
            "name": "Barsik",
            "age": 3,
            "features": ["ласковый", "рыжий", "ходит в капце"]
        })

    

except (PyMongoError, ValueError) as e:
    print(f"Connecting Error: {e}")