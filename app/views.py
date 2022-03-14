from flask import render_template, redirect,url_for, flash
from app import app, forms
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user
from .request import get_random_quotes


# Views
@app.route('/')
def index():

    # Getting random quotes

    random_quotes = get_random_quotes()
    print(random_quotes)

   
    title = 'Home - Quotes and more Quotes'
    return render_template('index.html', title = title, random = random_quotes )

@app.route('/login', methods = ['GET', 'POST'])    
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)      
    

@app.route('/register', methods = ['GET', 'POST'])    
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)       




      