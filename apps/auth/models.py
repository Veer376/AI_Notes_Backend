# here i have to connect with the mongo db and create a collection for the user
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://newyork:itsmearyaveer@clustor0.srbji.mongodb.net/?retryWrites=true&w=majority&appName=Clustor0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.sketch_ai
print('connected to the database')
