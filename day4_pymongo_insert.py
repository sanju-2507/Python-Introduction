from pydoc import cli
from click import MultiCommand
import pymongo

if __name__ == "__main__":
    print("Welcome to PyMongo !!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['Boss']
    myColl = db['Sample']
    print(client.list_database_names())
   
    dictionary0 = {'name': 'John', 'marks': 100}
    a= myColl.insert_one(dictionary0)
    print(a.inserted_id)


    dict1 = [
        {'name':'avds', 'class':3, 'city':'indore'},
        {'name':'gdsg', 'class':4, 'city':'bhopal'},
        {'name':'reye', 'class':5, 'city':'delhi'},
        {'name':'vbmv', 'class':6, 'city':'indore'},
        {'name':'avds', 'class':7, 'city':'mumbai'}
    ]
    y= myColl.insert_many(dict1)
    print(y.inserted_ids)

    a= myColl.find_one()
    print(a)

    b= myColl.find_one({'name':'reye'})
    print(b)

    c= myColl.find({'name':'avds'})
    print(c)


    for d in myColl.find():
        print(d)


    for e in myColl.find({}, {'city':'indore'}):
        print(e)


    for f in myColl.find({}, {'city':0}):
        print(f)


    prev= {"name" : "gdsg"}
    nextt={"$set" : { "number": 10 }}
    myColl.update_one(prev, nextt)

    for i in myColl.find():
        print(i)


    prev= {"name" : "gdsg"}
    nextt={"$set" : { "number": 10 }}
    myColl.update_many(prev, nextt)

    prev= {"name" : "gdsg"}
    nextt={"$set" : { "class": 10 }}
    myColl.update_many(prev, nextt)
    

    prev= {"name" : "vbmv"}
    nextt={"$set" : { "class": 10 }}
    aa=myColl.update_many(prev, nextt)
    print(aa.modified_count)


    rec={"name":"avds"}
    myColl.delete_one(rec)

    rec1={"name":"avds"}
    ab= myColl.delete_many(rec1)
    print(ab.deleted_count)