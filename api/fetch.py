from api.db_client import get_mongo_client
import os
from dotenv import load_dotenv
load_dotenv()

async def get_all():
    client = get_mongo_client()

    db = client[os.getenv("DB_NAME")]

    collection = db[os.getenv("COLLECTION_NAME")]
    documents =  list(collection.find())
   

    return documents
