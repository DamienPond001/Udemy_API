from db import db 

class ItemModel(db.Model):
   
   __tablename__ = "item"
   
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(80))
   price = db.Column(db.Float(precision = 2))
   
   store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
   store = db.relationship('StoreModel')
   
   def __init__(self, name, price, store_id):
      self.name = name
      self.price = price
      self.store_id = store_id
      
   def json(self):
      return {'name' : self.name, 'price' : self.price}
   
   
   @classmethod
   def find_by_name(cls, name):
      return cls.query.filter_by(name = name).first()  #ItemModel extends SQLAlchemy which handles all db connection. 
   # .query() says we are constructing a sql query, filter_by() creates the appropriate select
   # This returns an ItemModel object
       
      
   def save_to_db(self): # can update as well
      db.session.add(self)  #directly translate from object to row
      db.session.commit()
      
      
   def delete(self):
      db.session.delete(self)
      db.session.commit()
