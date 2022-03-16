
 
from urllib import response
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from hashlib import md5
from app import db, login_manager



# class User(db.Model):
#     def __init__(self,id,username,email):
#         self.id = id
#         self.username = username
#         self.email  = email

#         def set_password(self, password):
#             self.password_hash = generate_password_hash(password) 

#     def __repr__(self):
#         return f'User {self.id} {self.username}' 





@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True, nullable=False, index = True)
    email = db.Column(db.String(255),unique = True,index = True, nullable=False)    
    password_hash = db.Column(db.String(255), nullable=False)
    quotes = db.relationship('Quote', backref='author', lazy='dynamic')
   

    def __repr__(self):
        return f'User {self.id} {self.username}' 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  


    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

class Quote(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255),nullable=False)
    timestamp = db.Column(db.DateTime,index=True , default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Quote: {self.content}'   