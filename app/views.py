from urllib import request
from flask import render_template, redirect,url_for, flash
from app import app, forms, db
from app.models import  User, Quote
from app.forms import LoginForm, RegistrationForm, QuoteForm
from flask_login import current_user, login_user, login_required, logout_user
from .request import get_random_quotes

# Views

@app.route('/')
def index():
    db.session.query(User).delete()
    db.session.commit()

    # Getting random quotes

    random_quotes = get_random_quotes()

   
    title = 'Home - Quotes and more Quotes'
    return render_template('index.html', title = title, random = random_quotes, user = current_user )

@app.route('/login', methods = ['GET', 'POST'])    
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect('/')
    return render_template('login.html', title='Login', form=form, user=current_user)      
    

@app.route('/register', methods = ['GET', 'POST'])    
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {user.username}')
        return redirect(url_for('login'))
        
    return render_template('register.html', title='Register', form=form, user=current_user)    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/quote', methods = ['GET', 'POST'])
def quote():
    quoteForm = QuoteForm()
    quotes = Quote.query.all()

    if quoteForm.validate_on_submit():
        print('here')
        quote = Quote(content=quoteForm.content.data)
        db.session.add(quote)
        db.session.commit()
        return redirect('/quote')
        
    return render_template('quote.html', title='Quote', user=current_user, quoteForm=quoteForm, quotes=quotes)       

      