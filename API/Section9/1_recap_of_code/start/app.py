from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True     #Allows Flask extensions to raise their own errors
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

#claims add extra data when the JWT comes back to us
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
   #Note, identity is what we pass in in the UserLogin Resource
   if identity == 1: #This should be read in from the database
      return('is_admin' : True)
   return {'is_admin' : False}


#When the token expires
@jwt.expired_token_loader
def expired_token_callback():
   return jsonify({
         'description' : 'The token has expired',
         'error' : 'token_expired'
         }), 401
   
@jwt.invalid_token_loader
def invalid_toke_callback(error):
   return jsonify({
         'description' : 'signature verification failed', 
         'error' : 'invalid token'
         }), 401

@jwt_unauthorised_loader
   return jsonify({
         'description' : 'No access token', 
         'error' : 'authorisation required'
         }), 401


@jwt.needs_freah_token_loader
   return jsonify({
         'description' : 'token not fresh', 
         'error' : 'fresh token required'
         }), 401

@jwt.revoked_token_loader
   return jsonify({
         'description' : 'token revoked', 
         'error' : 'token_revoked'
         }), 401

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
