import pymongo
client =pymongo.MongoClient("mongodb+srv://ishwetak:Mynameissk@cluster0.skeefls.mongodb.net/?retryWrites=true&w=majority")
db = client.test
d = {
    "name":"Shweta",
    "email" : "shweta.kanhere@gmail.com",
    "surname" : "kanhere"
}
db1 = client['mongodbclass']
coll = db1['test']
coll.insert_one(d )