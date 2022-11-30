from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'Mapa_database.db')
app.config['SECRET_KEY'] = 'b0952ea2695b415757564fc0'
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



from markett import routes
from markett import models


