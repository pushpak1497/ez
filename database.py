from pymongo import MongoClient


client = MongoClient("mongodb+srv://pushpakvyas1497:<db_password>@ezcluster0.kfsuv.mongodb.net")
db = client.file_sharing_db
