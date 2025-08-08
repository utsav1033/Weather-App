import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(uri)
    db = client["weatherDB"]
    print("Connected successfully!")
    print("Collections:", db.list_collection_names())
except Exception as e:
    print("Connection failed:", e)
