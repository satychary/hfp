from flask import Flask
# app = Flask(__name__)


from flask import Flask
####from flask_cors import CORS #pip install this!!
app = Flask(__name__,static_folder='static')
####CORS(app)
#import requests
#from flask import Flask, request
#import json

# routes... how to 'route' the incoming req?

@app.route('/index.html')
def root():
    # print("Executing /")
#    return app.send_static_file('index.html')
    return "wow"






#@app.route("/")
#def hello():
#    return "Hello, OMGGod World!"
