from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

__version__ = "1.0.0 | 1.0.0"

def pinger(username, password, cluster_name) -> str:
    #taken directly from MongoDB's documentation
    username = quote_plus(username)
    password = quote_plus(password)
    cluster_name = quote_plus(cluster_name)

    uri = f"mongodb+srv://{username}:{password}@{cluster_name}.ygoqv7l.mongodb.net/?retryWrites=true&w=majority"
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return uri
    except Exception as e:
        print(e)
        exit(1)
    
def uploader(connection_string, sys_info) :    
    # create a client and connect to the server
    client = MongoClient(connection_string, server_api=ServerApi('1'))
    
    # link to database then collection
    database = client.system_info
    system_inf_collection = database.system_info_collection
    
    # upload fetched system info data to database
    system_inf_id = system_inf_collection.insert_one(sys_info).inserted_id
    print(f"MongoDB upload ID: {system_inf_id}")