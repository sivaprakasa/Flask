import pymongo  #install to pymongo

mongocon = pymongo.MongoClient("mongodb://localhost:27017")   #mongodb localpath

mydatabase = mongocon["TITO"] #create database

mycollection = mydatabase["Employee"]  #create collection

#create collection document
mydoc = {"name":"kishore","age":21,"city":"madurai"},{"name":"sanjay","age":21,"city":"chennai"},{"name":"renuka","age":21,"city":"sivakasi"}

#insert method
insertmy = mycollection.insert_many(mydoc)