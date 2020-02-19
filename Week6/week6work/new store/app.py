from flask import Flask
from flask import render_template
from week6work.test import users
from forms import LoginForm

app = Flask(__name__)
users.create_database()
app.config['SECRET_KEY'] = 'poop'




@app.route('/login')
def login():
    form = LoginForm()
    login = render_template('login.html',form = form)
    return login
    users = users.load_database


@app.route('/')
def index_page():
    index = render_template('index.html')
    return index



if __name__ == '__main__':
    app.run()