from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import  validators
import wtforms
import flask_wtf

class LoginForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", [validators.Length(min=4, max=20)])
    password = wtforms.PasswordField("Password", [validators.Length(min=4, max=20)])
    print (username,password)