'''This was created after installing virtualenv. This allows use to create a virtual environment that mimics 
a fresh Python install. This ensures that any updates to packages don't affect previous applications built on previous package versions.

Run: conda create -n venv python=3.5.0 anaconda
to create a virtual env called venv with python 3.5.0

conda activate venv
conda deactivate'''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret_key"  #this should be long and complicated in a production sense
api = Api(app)


@app.before_first_request
def create_tables():  #Creates the tables it sees through the imports
   db.create_all()


jwt = JWT(app, authenticate, identity)  
'''
JWT creates an endpoint /auth. When we call /auth we send a username and password, which is passed on to authenticate and identity
If authenticate returns a user, and that is the identity and the /auth endpoint returns a JWT
The JWT calls the identity function which gets the correct id and returns the user
'''

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')   
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/item_name
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':    #This ensures that this is not run if app.py is imported, but only when called
   from db import db
   db.init_app(app)
   app.run(port=5000, debug=True)  #debug gives better error messages