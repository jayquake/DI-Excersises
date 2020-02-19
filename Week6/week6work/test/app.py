from flask import Flask
from flask import render_template
import users
from forms import LoginForm
from flask import request
from flask import session
from flask import flash

app = Flask(__name__)
users = users.create_database()
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    html = render_template('index.html')
    return html

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    login =render_template('login.html',form = form)
if request.form['password'] == 'password' and request.form['username'] == 'admin':
    session['logged_in'] = True
else:
    flash('wrong password!')


if __name__ == '__main__':
    app.run()