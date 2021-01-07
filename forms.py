from flask_wtf_ext import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo

from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("User with that name already exist")


def email_exist(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("User with that email already exists")


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^a-zA-Z0-9_]+$',
                message=("Username should be one word letters, "
                         "numbers and underscores only")
            ),
            name_exists
        ]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            email_exist
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6),
            EqualTo('password2', message='Passwords must watch')
        ]
    )
    password2 = StringField(
        'Confirm Password',
        validators=[
            DataRequired()
        ]
    )


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(), Email()
        ]
    )
    password = StringField(
        'Password',
        validators=[DataRequired()]
    )


class PostForm(FlaskForm):
    content = TextAreaField('what\'s on your mind', validators=[DataRequired()])
