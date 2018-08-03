from user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
   user = User.find_by_username(username)
   if user is not None and safe_str_cmp(user.password, password):   #safe_str_cmp() alleviates issues with string comparison
      return user
  
#identity function is unique to flask JWT
#payload is the contents on the JWT Token
def identity(payload):
   user_id = payload['identity']
   return User.find_by_id(user_id)
   
   
   
   
   
   