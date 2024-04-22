import pymongo

dbName="mydatabase18"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient[dbName]

dblist = myclient.list_database_names()


if dbName in dblist:
  print("The database exists.")

print(myclient.list_database_names())


print(mydb.list_collection_names())

collist = mydb.list_collection_names()
mycol = mydb["customers"]

if "customers" in collist:
  print("The collection exists.")

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

for x in mycol.find():
  print(x)


mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)


mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

x = mycol.find_one()

print(x)

print("_id: 0, name: 1, address: 1")
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

print("address: 0")

for x in mycol.find({},{ "address": 0 }):
  print(x)


myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

print(myquery)
for x in mydoc:
  print(x)


myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)
print(myquery)
for x in mydoc:
  print(x)


myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)
print(myquery)
for x in mydoc:
  print(x)


mydoc = mycol.find().sort("name")
print("mycol.find().sort(name)")
for x in mydoc:
  print(x)


mydoc = mycol.find().sort("name", -1)
print("mycol.find().sort(name,-1)")
for x in mydoc:
  print(x)


myquery = { "address": "Mountain 21" }
print("delete_one(myquery)")

mycol.delete_one(myquery)


myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")


x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

mycol.drop()
print(" mycol.drop()")

mycol = mydb["customers"]



mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

print ("customers after the update:")
for x in mycol.find():
  print(x)


myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")


myresult = mycol.find().limit(5)

print("the result limited by 5")
for x in myresult:
  print(x)
