##from markett import db
from flask import Flask, render_template
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy
import os
from markett import app, login_manager
from markett import bcrypt
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'Mapa_database.db')

db = SQLAlchemy(app)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_adress = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


    @property 
    def password(self):
        return self.password

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]}, {str(self.budget)[-3:]}₳'
        else:
            return f"{self.budget}"






    @password.setter
    def password (self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    


    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    
    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

     


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    map_title = db.Column(db.String(length=256), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner= db.Column(db.Integer(), db.ForeignKey('user.id'))

    def buy(self, user):
     self.owner = user.id
     user.budget -= self.price
     db.session.commit()

app.app_context().push()
db.create_all()
db.session.commit()



def __repr__(self):
    return f'Item {self.name}'





#item3 = Item(map_title="Map of Bartolomeo Pareto (1455)", price =987, barcode="987654356123", description="Ancient Map")
#from market import app, db
#app.app_context().push()
#db.create_all()
#db.session.add(item3)
#db1.session.commit()
