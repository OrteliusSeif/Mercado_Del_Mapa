from markett import app
from flask import render_template, redirect, url_for, flash
from markett.models import Item, User
from markett.forms import RegisterForm
from markett import db




@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
    #items = [
    #{'id': 1, 'map_title': 'Atlas Maior', 'barcode': '893212299897', 'price': 500},
    #{'id': 2, 'map_title': 'Fra Mauro map of the world', 'barcode': '123985473165', 'price': 900},
   # {'id': 3, 'map_title': 'Anaximander world map', 'barcode': '231985128446', 'price': 150}
    #]
    

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adress= form.email_adress.data, 
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors !={}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')


    return render_template('register.html', form=form)



