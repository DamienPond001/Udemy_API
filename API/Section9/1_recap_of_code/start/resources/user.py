from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
      create_access_token,
      create_refresh_token,
      jwt_refresh_token_required,
      get_jwt_identity
      )
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class User(Resource):
   @classmethod
   def get(cls, user_id):
      user = UserModel.find_by_id(user_id)
      
      if user is None:
         return {'message' :'user not found'}, 404
      else:
         return user.json()
         
   
   @classmethod
   def delete(cls, user_id):
      user = UserModel.find_by_id(user_id)
      
      if user is None:
         return {'message' : 'User not found'}, 404
      else:
         user.delete_from_db()
         return {'message' : 'User deleted'}

class UserLogin(Resource):
   parser = reqparse.RequestParser()
   parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
   parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
   
   def post(self):
      data = self.parser.parse_args()
      
      user = UserModel.find_by_username(data['username'])
      
      #This is what 'authenticate()' used to do
      if user is not None and safe_str_cmp(user.password, data['password']):
         #What the 'identity()' function used to do
         access_token = create_access_token(identity = user.id, fresh = True)
         refresh_token = create_refresh_token(user.id)
         
         return {
               'access_token' : access_token,
               'refresh_token' : refresh_token
               }, 200
      else:
         return {'message' : 'Invalid credentials'}, 401

class TokenRefresh(Resource):
   @jwt_refresh_token_required
   def post(self):
      current_user = get_jwt_identity()
      new_token = create_access_token(identity = current_user, fresh = False)
      return {'access_token' : new_token}, 200