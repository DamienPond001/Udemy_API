# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:04:52 2018

@author: Damien
"""

from flask import Flask

app = Flask(__name__)    #unique __name__ - special python variable

#What requests we need to understand
@app.route('/') #http://www.google.com/ - '/' represents the home page [http://www.google.com/maps represents a '/maps' endpoint]
def home():  #whatever this does it must return a reponse to the browser
   return "Hello, world!"

app.run(port=5000) #app runs on port/area of computer that the computer sends and recieces requests

#run from conda "python app.py"
#copy 127.0.0.1:5000 into browswer (127.0.0.1 is the IP reserved fro your computer)