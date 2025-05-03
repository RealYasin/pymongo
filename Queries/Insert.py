# MongoDB

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
disc={"Name":"Tejju","Age":21}
x=mycol.insert_one(disc)
print(x)
