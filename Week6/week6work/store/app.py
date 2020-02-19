from flask import Flask
import flask
from flask import render_template
import db
app = Flask(__name__)

db.create_database()

@app.route("/")
@app.route("/products")
def products_page():

    products = db.load_database()
    template = render_template('home.html' )

    return flask.render_template_string(template, products = products)


app.run(debug=True)