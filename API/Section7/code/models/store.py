from db import db 

class StoreModel(db.Model):
   
   __tablename__ = "stores"
   
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(80))
   
   items = db.relationship('ItemModel', lazy = 'dynamic')
   
   def __init__(self, name):
      self.name = name
      
   def json(self):
      return {'name' : self.name, 'items' : [item.json() for item in self.items.alls()]} #the lazy = 'dynamic' arg means items is a query builder and not an item list
   
   
   @classmethod
   def find_by_name(cls, name):
      return cls.query.filter_by(name = name).first()  #ItemModel extends SQLAlchemy which handles all db connection. 
   # .query() says we are constructing a sql query, filter_by() creates the appropriate select
   # This returns an ItemModel object
       
      
   def save_to_db(self): # can update as well
      print("here")
      db.session.add(self)  #directly translate from object to row
      db.session.commit()
      
      
   def delete(self):
      db.session.delete(self)
      db.session.commit()
