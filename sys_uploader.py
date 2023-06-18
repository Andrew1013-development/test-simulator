from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import certifi

__version__ = "1.0.2 | 1.0.1"

def pinger(username, password, cluster_name, debug_short, debug_full) -> str:
    #taken directly from MongoDB's documentation
    username = quote_plus(username)
    password = quote_plus(password)
    cluster_name = quote_plus(cluster_name)

    uri = f"mongodb+srv://{username}:{password}@{cluster_name}.ygoqv7l.mongodb.net/"
    
    # Create a new client and connect to the server
    client = MongoClient(uri,tlsCAFile = certifi.where(),server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        print("Establishing connection to database.....")
        client.admin.command('ping')
        if debug_short:
            print("Pinged your deployment. You successfully connected to MongoDB!")
        print("Connection established to database.")
        return uri
    except Exception as e:
        print(e)
        exit(1)
    
def uploader(connection_string, sys_info, debug_short, debug_full) :    
    # create a client and connect to the server
    client = MongoClient(connection_string, server_api=ServerApi('1'))
    
    # link to database then collection
    database = client.system_info
    system_inf_collection = database.system_info_collection
    
    # upload fetched system info data to database
    system_inf_id = system_inf_collection.insert_one(sys_info).inserted_id
    if debug_full:
        print(f"MongoDB upload ID: {system_inf_id}")
