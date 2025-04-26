# Inserting data using GUI/User Interface

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
name=input("Enter your Name= ")
age=int(input("Enter your Age= "))
disc={"Name":name,"Age":age}
x=mycol.insert_one(disc)
print(x)
