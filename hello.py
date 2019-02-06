 # import Flask class
 # WSGI (Web Server Gateway Interface) 
 
from flask import Flask
 # __name__
app = Flask(__name__)

# route() url trigeer function
# root
@app.route('/')

def hello_world():
  return "<html><body><h2>Hello World!</h2></body></html>"