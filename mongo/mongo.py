#from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os


## Comment out when running locally
client = MongoClient(os.getenv("MONGOURL"))
db = client.test    #Select the database
db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))
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
  
def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')


def run_sample():
  lists_all()
  key = addTask('yoav','test123','211221','high')
  print(key)
  lists_all()
  remove(key)
  lists_all()

if __name__ == "__main__":

    run_sample()
