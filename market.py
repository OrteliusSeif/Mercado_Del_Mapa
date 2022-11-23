from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import os





basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'Carto_database.db')

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

















@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market')
def market_page():
    items = Item.query.all()
    #items = [
    #{'id': 1, 'map_title': 'Atlas Maior', 'barcode': '893212299897', 'price': 500},
    #{'id': 2, 'map_title': 'Fra Mauro map of the world', 'barcode': '123985473165', 'price': 900},
   # {'id': 3, 'map_title': 'Anaximander world map', 'barcode': '231985128446', 'price': 150}
    #]






    return render_template('market.html', items=items)



app.debug = True
app.run(debug=True, use_debugger=False, use_reloader=False)