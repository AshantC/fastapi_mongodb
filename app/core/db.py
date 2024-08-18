
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib

uri = "mongodb+srv://<username>:<password>@personal0.6ecna.mongodb.net/?retryWrites=true&w=majority&appName=personal0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# create database
db = client.todo_db


# create collection
collection = db["todo_data"]


# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)