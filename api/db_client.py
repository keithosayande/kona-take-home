from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

def get_mongo_client():
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        raise ValueError("MONGODB_URI not set in environment variables")
    client = MongoClient(mongo_uri, server_api=ServerApi(
        version="1", strict=True, deprecation_errors=True))
    return client
