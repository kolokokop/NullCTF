from pymongo import MongoClient
import os

discord_token = os.environ['DISCORD_TOKEN']
mongodb_connection = os.environ['MONGODB_CONNECTION']

client = MongoClient(mongodb_connection)

ctfdb = client['ctftime'] # Create ctftime database
ctfs = ctfdb['ctfs'] # Create ctfs collection

teamdb = client['ctfteams'] # Create ctf teams database

serverdb = client['serverinfo'] # configuration db
