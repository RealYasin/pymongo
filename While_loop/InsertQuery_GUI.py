# Inserting data using GUI/User Interface with while loop

import pymongo as pm
mydata=pm.MongoClient("mongodb://localhost:27017/")
mydb=mydata["MongoDB"]
mycol=mydb["Data"]
i=0
num=int(input("Enter the Number= "))
while i<=num:
    name=input("Enter your Name= ")
    age=int(input("Enter your Age= "))
    disc={"Name":name,"Age":age}
    x=mycol.insert_one(disc)
    i=i+1
print(x)
