from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email 

class UserInfoForm(FlaskForm):
    name = StringField('name', validators = [DataRequired()])
    phone_number = StringField('phone number', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    confirm_pass = PasswordField('confirm password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()