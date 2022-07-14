from petfax import create_app
app = create_app()
#Pt1 code
'''
# config
from flask import Flask
app = Flask(__name__)

#index route
@app.route('/')
def index():
    return 'Hello this is PetFax2!'

#pets index route
@app.route('/pets')
def pets():
    return 'These are the pets we have for adoption.'

#picture route
@app.route('/pics')
def pics():
    return 'This is where pictures will be.'
'''