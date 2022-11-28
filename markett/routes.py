from markett import app
from flask import render_template
from markett.models import Item, User



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



