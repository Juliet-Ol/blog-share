from flask import render_template, redirect,url_for, flash
from app import app, forms
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user


# Views
@app.route('/')
@app.route('/index')
def index():

    return render_template ('index.html',title = 'home')

@app.route('/login', methods = ['GET', 'POST'])    
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)      
    

@app.route('/register', methods = ['GET', 'POST'])    
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)       




      