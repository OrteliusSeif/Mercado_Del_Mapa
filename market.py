from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')



app.debug = True
app.run(debug=True, use_debugger=False, use_reloader=False)