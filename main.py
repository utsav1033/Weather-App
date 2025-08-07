"""This module handles MongoDB database connection using environment variables."""

import os  # standard library
from pymongo import MongoClient  # third-party
from dotenv import load_dotenv  # third-party

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database()
