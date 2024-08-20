#Connect python to mongodb service of aws using lambda


import pymongo
import json

def lambda_handler(event, context):
    # MongoDB connection details
    mongo_uri = "mongodb://username:password@your-mongodb-host:27017/your-database"
    
    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client['your-database']
    collection = db['your-collection']

    # Perform a simple query (example)
    data = collection.find_one({"key": "value"})

    # Close the MongoDB connection
    client.close()

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }


