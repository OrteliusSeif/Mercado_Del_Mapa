from markett import db
from flask import Flask, render_template
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy
import os
from markett import app





#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'Carto_database.db')

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_adress = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    map_title = db.Column(db.String(length=256), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner= db.Column(db.Integer(), db.ForeignKey('user.id'))

#app.app_context().push()
#db.create_all()
#db.session.commit()



def __repr__(self):
    return f'Item {self.name}'



#item3 = Item(map_title="Map of Bartolomeo Pareto (1455)", price =987, barcode="987654356123", description="Ancient Map")
#from market import app, db
#app.app_context().push()
#db.create_all()
#db.session.add(item3)
#db1.session.commit()
