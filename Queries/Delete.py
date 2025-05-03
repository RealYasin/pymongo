# Delete Query using python

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
x={"Name":"xyz"}
mycol.delete_one(x)
print("Task Done")
