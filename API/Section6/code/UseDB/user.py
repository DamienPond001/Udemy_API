import sqlite3
from flask_restful import Resource, reqparse

class User:
     
   def __init__(self, _id, username, password):
      self.id = _id
      self.username = username
      self.password = password
      
   @classmethod
   def find_by_username(cls, username):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      select_query = "SELECT * FROM users WHERE username = ?"
      
      result = cursor.execute(select_query, (username,))   #input needs to be a tuple and single value tuples need a comma
      row = result.fetchone()
      
      if row is not None:
         user = cls(*row)   #exapnds as row[0], row[1], row[2]
      else:
         user = None
                  
      connection.close()
      return user
   
   @classmethod
   def find_by_id(cls, _id):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      select_query = "SELECT * FROM users WHERE id = ?"
      
      result = cursor.execute(select_query, (_id,))   #input needs to be a tuple and single value tuples need a comma
      row = result.fetchone()
      
      if row is not None:
         user = cls(*row)   #exapnds as row[0], row[1], row[2]
      else:
         user = None
                  
      connection.close()
      return user
      

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
      new_user = UserRegister.parser.parse_args()
      
      if User.find_by_username(new_user['username']) is not None:
         return {"message" : "User already created"}, 400
      
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      query = "INSERT INTO users VALUES (NULL, ?, ?)"
      
      cursor.execute(query, (new_user['username'], new_user['password']))
      
      connection.commit()
      connection.close()
      
      return {"message":"new user added"}, 201
      