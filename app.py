from functools import wraps
from http import client
from pydoc import cli
from functools import wraps
import socket
from flask import Flask, render_template, session, redirect
import pymongo
import os


app = Flask(__name__)
app.secret_key = b'\xe5\xf1!\xde`\xf2\xd2vCh\xeeZ\xb5\x02\x02.'


# Database
# for remote web connection 
# client = pymongo.MongoClient(r"mongodb+srv://aditya:Adi8877@cluster0.wjpj2.mongodb.net/?retryWrites=true")

# for kubernetes deployment
uri = "mongodb://"+"mongodb-service"+":"+str(27017)
client = pymongo.MongoClient(uri)
database = client['user_login_system']
collection = database['users']

# for docker deplotment
# client = pymongo.MongoClient("mongodb://"+os.environ["MONGODB_SERVICE_PORT"],
#                             username=os.environ["MONGO_INITDB_ROOT_USERNAME"],
#                             password=os.environ["MONGO_INITDB_ROOT_PASSWORD"],
#                             authSource="admin"
#                             )


# db = client.user_login_system
db = database

# Decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)