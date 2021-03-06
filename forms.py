from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField( 'Username',
                            validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField( 'Email',
                            validators=[DataRequired(),Email()])
    password = StringField( 'Password',
                            validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password = StringField( 'Confirm Password',
                            validators=[DataRequired(),Length(min=6,max=20),EqualTo('password')])
    submit = SubmitField( 'Sign Up')

class LoginForm(FlaskForm):
    email = StringField( 'Email',
                            validators=[DataRequired(),Email()])
    password = StringField( 'Password',
                            validators=[DataRequired()])
    submit = SubmitField( 'Login')