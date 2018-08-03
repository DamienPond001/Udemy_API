from user import User
from werkzeug.security import safe_str_cmp

#some database
users = [
      User(1, "bob", "asdf"), 
      User(2, "Damien", "bitches")
      ]


#below allows us to find the user by username or ID without having to iterate over the above list
username_mapping = {u.username : u for u in users}  #list comprehension where the function is a key:value pair
userid_mapping = {u.id : u for u in users}

def authenticate(username, password):
   user = username_mapping.get(username, None)  #note that this is the same as the [] notation, but allows a default value
   if user is not None and safe_str_cmp(user.password, password):   #safe_str_cmp() alleviates issues with string comparison
      return user
  
#identity function is unique to flask JWT
#payload is the contents on the JWT Token
def identity(payload):
   user_id = payload['identity']
   return userid_mapping.get(user_id, None)
   
   
   
   
   
   