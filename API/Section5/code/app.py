'''This was created after installing virtualenv. This allows use to create a virtual environment that mimics 
a fresh Python install. This ensures that any updates to packages don't affect previous applications built on previous package versions.

Run: conda create -n venv python=3.5.0 anaconda
to create a virtual env called venv with python 3.5.0

conda activate venv
conda deactivate'''

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "secret_key"  #this should be long and complicated in a production sense
api = Api(app)

jwt = JWT(app, authenticate, identity)  
'''
JWT creates an endpoint /auth. When we call /auth we send a username and password, which is passed on to authenticate and identity
If authenticate returns a user, and that is the identity and the /auth endpoint returns a JWT
The JWT calls the identity function which gets the correct id and returns the user
'''

items = []

class Item(Resource):
   @jwt_required()
   def get(self, name):
      item = next(filter(lambda x: x['name'] == name, items), None)  #if next produces nothing, return None
      return {"item" : item}, 200 if item is not None else 404
   
   def post(self, name):
      #Note that the 'Header' and 'Body' need to be set
      if next(filter(lambda x: x['name'] == name, items), None) is not None:
         return {"message" : "an item with name '{}' already exists.".format(name)}, 400 #400 = bad request
         
      data = request.get_json() #args: force:Forces the content header, silent: returns None (generally don't use)
      item  = {'name' : name, 'price' : data['price']}
      items.append(item)
      
      return item, 201 #201 is code for created

class ItemList(Resource):
   def get(self):
      return{"items" : items}
   
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/item_name
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)  #debug gives better error messages