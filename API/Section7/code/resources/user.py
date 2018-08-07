import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

#This allows us to create a flask_restful endpoint to input new users
class UserRegister(Resource):     
   parser = reqparse.RequestParser()  #This prevents code duplication and now belongs to the Item class
   parser.add_argument('username',      
                        type = str, 
                        required = True,
                        help = "This field cannot be left blank")
   parser.add_argument('password',      
                        type = str, 
                        required = True,
                        help = "This field cannot be left blank") 
   
   
   def post(self):
      data = UserRegister.parser.parse_args()
      
      if UserModel.find_by_username(data['username']) is not None:
         return {"message" : "User already created"}, 400
      
      user = UserModel(data['username'], data['password'])  #(**data)
      user.save_to_db()
      
      return {"message":"new user added"}, 201
      