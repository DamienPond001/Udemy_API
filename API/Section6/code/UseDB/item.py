from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
   parser = reqparse.RequestParser()  #This prevents code duplication and now belongs to the Item class
   parser.add_argument('price',       
                        type = float, 
                        required = True,
                        help = "This field cannot be left blank")   
   
   
   @jwt_required()
   def get(self, name):
      item = self.find_by_name(name)
      
      #http://127.0.0.1:5000/item/wine?price=17 will pass 17 to the args
      #args = Item.parser.parse_args()
      #print(args['price'])
      
      
      if item is not None:
         return item, 200
      else:
         return {"message" : "Item not found"}, 404

   @classmethod
   def find_by_name(cls, name):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      select_query = "SELECT * FROM items WHERE name = ?"
      result = cursor.execute(select_query, (name,))
      item_in_db = result.fetchone()
      connection.close()
      
      if item_in_db is not None:
         return {'item' : {'name' : item_in_db[0], 'price': item_in_db[1]}}
      
   #We could use the get() method but that requires a JWT 
   #Thus we use the alternative class method
   def post(self, name):   
      
      item = self.find_by_name(name)
      if item is not None:
         return {"message":"item already in database"}, 400
      
      data = Item.parser.parse_args()
      item = {'name' : name, 'price': data['price']}
      
      try:
         self.insert_item(item)
      except:
         return {"message" : "An error occurred"}, 500
      
      return {'name' : name, 'price' : data['price']}, 201 #201 is code for created
   
   
   @classmethod
   def insert_item(cls, item):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      insert_query = "INSERT INTO items VALUES (?, ?)"
      cursor.execute(insert_query, (item['name'], item['price']))
      
      connection.commit()
      connection.close()
   
   def delete(self, name):

      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      delete_query = "DELETE FROM items WHERE name = ?"
      
      cursor.execute(delete_query, (name,))
      
      connection.commit()
      connection.close()
      
      return {"message" : "Item deleted"}
   
   def put(self, name):

      item = self.find_by_name(name)
      data = Item.parser.parse_args()
      updated_item = {'name' : name, 'price': data['price']}

      if item is None:
         try:
            self.insert_item(updated_item)
         except:
            {"message" : "an error occurred"}, 500
      else:
         try:
            self.update(updated_item)
         except:
            {"message" : "an error occurred"}, 500         

      return updated_item, 201 #201 is code for created
      

   @classmethod
   def update(cls, item):
         connection = sqlite3.connect('data.db')
         cursor = connection.cursor()
         
         insert_query = "UPDATE items SET price = ? WHERE name = ?"
         cursor.execute(insert_query, (item['price'], item['name']))
         
         connection.commit()
         connection.close()
      


class ItemList(Resource):
   def get(self):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      
      query = "SELECT * FROM items"
      
      result = cursor.execute(query)
      items = result.fetchall()
      connection.close()
      
      if items is not None:
         return {'items' : items}
      else:
         return {"message" : "No items in database"}
      