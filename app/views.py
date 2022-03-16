from urllib import request
from flask import render_template, redirect,url_for, flash
from app import app, forms, db
from app.models import  User
from app.forms import LoginForm, RegistrationForm, QuoteForm
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

    if form.validate_on_submit():
        print('here')
        user = User(id=1, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {user.username}')
        return redirect(url_for('login'))
        
    return render_template('register.html', title='Register', form=form)    


@app.route('/_quote', methods = ['GET', 'POST'])    
def quote():
    form = QuoteForm()

    if form.validate_on_submit():
        print('here')
        user = User(id=1, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Quote {user.username}')
        return redirect(url_for('login'))
        
    return render_template('_quote.html', title='Quote', form=form)       







      