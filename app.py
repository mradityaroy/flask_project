from functools import wraps
from http import client
from pydoc import cli
from functools import wraps
from flask import Flask, render_template, session, redirect
import pymongo


app = Flask(__name__)
app.secret_key = b'\xe5\xf1!\xde`\xf2\xd2vCh\xeeZ\xb5\x02\x02.'


# Database
# client = pymongo.MongoClient(r"mongodb+srv://aditya:Adi8877@cluster0.wjpj2.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient(host='test_mongodb',
                        port=27017, 
                        username='root', 
                        password='pass',
                        authSource="admin")

db = client.user_login_system

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

