#from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
import config

MONGOURL = config.settings['MONGOURL']
MONGO_USERNAME = config.settings['MONGO_USERNAME']
MONGO_PASSWORD = config.settings['MONGO_PASSWORD']

## Comment out when running locally
client = MongoClient(MONGOURL)
db = client.test    #Select the database
db.authenticate(name=MONGO_USERNAME,password=MONGO_PASSWORD)
todos = db.todo #Select the collection

def lists_all():
  todos_l = todos.find()
  print(todos_l)
  
def addTask (aName,aDesc,aDate,aPr):
	#Adding a Task
	name=aName
	desc=aDesc
	date=aDate
	pr=aPr
	key = todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
	print("added task:"+key)
	return key

  

def remove (key):
	todos.remove({"_id":ObjectId(key)})
	return redirect("/")
  

def run_sample():
  lists_all()
  key = addTask('yoav','test123','211221','high')
  print(key)
  lists_all()
  remove(key)
  lists_all()

if __name__ == "__main__":

    run_sample()
