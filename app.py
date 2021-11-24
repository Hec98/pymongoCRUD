from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['testDB']
collection = db['products']

collection.insert_one({"name": "kuyboard", "price": 300})
