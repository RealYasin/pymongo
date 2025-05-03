# Update Query using python

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
x={"Name":"Mir Yasin Ali"}
y={"$set":{"Fees":50000}}
mycol.update_one(x,y)
print("Fees has been updated")
