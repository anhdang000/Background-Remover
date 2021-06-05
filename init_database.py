import pymongo
from pymongo import MongoClient
import json

# Database initialization
client = MongoClient(host='mongodb',
                        port=27017, 
                        username='root', 
                        password='pass',
                    authSource="admin")
db = client["image_db"]

with('mongodb/init.json', 'r') as f:
    data = json.load(f)

db.image_tb.insert_many(data)