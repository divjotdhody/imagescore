from pymongo import MongoClient
# pprint library is used to make the output look more pretty
# from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

uri = 'mongodb+srv://bevyuser:bevypassword@cluster0.d9pnz.mongodb.net/ImageCounter?retryWrites=true&w=majority'
client = MongoClient(uri)
print(client)
