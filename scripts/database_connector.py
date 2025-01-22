from pymongo import MongoClient

def get_latest_trends():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["twitter_trends"]
    collection = db["trends"]
    
    # Fetch the most recent entry
    result = collection.find_one(sort=[("timestamp", -1)])
    
    return result
