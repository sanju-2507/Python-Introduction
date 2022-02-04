from pydoc import cli
import pymongo

if __name__ == "__main__":
    print("Welcome to PyMongo !!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)