# Find Query using python GUI

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
find=int(input("Enter your index value= "))
x=mycol.find()
print(x[find])
