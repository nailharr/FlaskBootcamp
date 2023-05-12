from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class Lf(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("e-mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField("Password confirm", validators=[DataRequired()])
    remember_me = BooleanField("Remember me", validators=[DataRequired()])
    submit = SubmitField("Register", validators=[DataRequired()])
