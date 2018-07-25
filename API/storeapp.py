# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:43:47 2018

@author: Damien
"""

from flask import Flask, jsonify, request, render_template

#NOTE on JSON: JSON are essentially dictionaries but in string format. Thus we need to convert of Python dicts to text
app = Flask(__name__)    #unique __name__ - special python variable
stores = [
      {
         'name': 'My Store',
         'items': [
               {
                  'name':'My Item',
                  'price':15.99
               }
            ]
      }
]

@app.route('/')
def home():
   return render_template('index.html')   #Looks in template folder

#POST - recieves data
#GET - send data back

##End points we are going to define
#POST /store data: {name:}
@app.route('/store', methods = ['POST'])   #default to GET
def create_store():
   request_data = request.get_json()
   new_store = {
            'name': request_data['name'],
            'items' : []
         }
   
   stores.append(new_store)
   return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')    #<string:name> is a flask keyword
def get_store(name):
   for store in stores:
      if store['name'] == name:
         return jsonify(store)
      else:
         return jsonify({'message' : 'No such store'})

#GET /store
@app.route('/store')
def get_stores():
   return jsonify({'stores' : stores})   #convert list to dictionary

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])   #default to GET
def create_item(name):
   request_data = request.get_json()
   for store in stores:
      if store['name'] == name:
         new_item = {
            'name' : request_data['name'],
            'price' : request_data['price']
         }
         store['items'].append(new_item)
         return jsonify(new_item)
      else:
         return jsonify({"message" : " No such store"})
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')    #<string:name> is a flask keyword
def get_item_in_store(name):
   for store in stores:
      if store['name'] == name:
         return jsonify({'items' : store['items']})
      else:
         return jsonify({'message' : 'No such store'})


app.run(port=5000) #app runs on port/area of computer that the computer sends and recieces requests

#run from conda "python app.py"
#copy 127.0.0.1:5000 into browswer (127.0.0.1 is the IP reserved fro your computer)