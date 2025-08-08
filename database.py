"""Database connection setup for the Weather App."""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["weatherDB"]   # database
collection = db["weather"] # collection


