# Find Query using python with while loop to see multiple results

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
x=mycol.find()
i=0
while i<=8:
    print(x[i])
    i=i+1
