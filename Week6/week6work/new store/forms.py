import flask_wtf
from  wtforms import validators
import wtforms

class LoginForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", [validators.Length(min=4, max=20)])
    password = wtforms.PasswordField("Password", [validators.Length(min=4, max=20)])
    print (username,password)