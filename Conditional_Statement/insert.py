# Conditional Statement

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
name=input("Enter the Name= ")
age=int(input("Enter your Age= "))
fees=int(input("Enter your Fees= "))
if age<=18:
    print("Not a valid age")
else:
    disc={"Name":name,"Age":age,"Fees":fees}
    x=mycol.insert_one(disc)
    print("Data inserted")
