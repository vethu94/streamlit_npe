import pymongo
import datetime
import names

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
id_collection = db["id_counter"]
collection = db["mycollection"]

# Create a function to get the next ID value
def get_next_id():
    counter = id_collection.find_one_and_update(
        {"_id": "my_collection_counter"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=pymongo.ReturnDocument.AFTER
    )
    return counter["seq"]

# Create a document
document = {
    "_id": get_next_id(),
    "name": names.get_full_name(),
    "timestamp": datetime.datetime.utcnow(),
    "testcase": "test_case_1",
    "bootuptime": 120.5,
    "connecttime": 10.2,
    "firmware": "v1.0.0"
}

# Insert the document into the collection
collection.insert_one(document)

# Retrieve the inserted document
result = collection.find_one(document)

print(result)