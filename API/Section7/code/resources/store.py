from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
   def get(self, name):
      store = StoreModel.find_by_name(name)
      
      if store is None:
         return {"message" : "No such store"}, 404
      
      return store.json()
   
   def post(self, name):
      
      store = StoreModel.find_by_name(name)
      print(store)
      if store is not None:
         return {"message": "Store exists"} , 400
      
      store = StoreModel(name)
      try:
         store.save_to_db()
      #except Exception as e: print(e)
      except:
         return {"message" : "An error occurred"}, 500
      
      return {"message" : "Store added"}, 201
   
   def delete(self, name):
      store = StoreModel.find_by_name(name)
      store.delete()
      
      return {"message" : "Store deleted"}
      pass
   
   
class StoreList(Resource):
   def get(self):
      return {"stores" : [store.json() for store in StoreModel.query().all()]}