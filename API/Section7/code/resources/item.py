from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
   parser = reqparse.RequestParser()  #This prevents code duplication and now belongs to the Item class
   parser.add_argument('price',       
                        type = float, 
                        required = True,
                        help = "This field cannot be left blank")
   parser.add_argument('store_id',       
                        type = int, 
                        required = True,
                        help = "This field cannot be left blank")   
   
   
   @jwt_required()
   def get(self, name):
      item = ItemModel.find_by_name(name)
    
      if item is not None:
         return item.json(), 200
      else:
         return {"message" : "Item not found"}, 404

      
   #We could use the get() method but that requires a JWT 
   #Thus we use the alternative class method
   def post(self, name):   
      
      item = ItemModel.find_by_name(name)
      if item is not None:
         return {"message":"item already in database"}, 400
      
      data = Item.parser.parse_args()
      item = ItemModel(name, data['price'], data['store_id'])
      
      try:
         item.save_to_db()
      except:
         return {"message" : "An error occurred"}, 500
      
      return item.json(), 201 #201 is code for created
   
   
   def delete(self, name):

      item = Item.find_by_name(name)
      if item is not None:
         item.delete()
      
      return {"message" : "Item deleted"}
   
   def put(self, name):

      item = ItemModel.find_by_name(name)
      data = Item.parser.parse_args()

      if item is None:
         item = ItemModel(name, data['price'], data['store_id'])
      else:
         item.price = data['price']       

      item.save_to_db()
      return item.json(), 201 #201 is code for created
           


class ItemList(Resource):
   def get(self):
      return {'items' : [x.json() for x in ItemModel.query.all()]} #list(map(lambda x: x.json(), ItemModel.query.all()))
      
