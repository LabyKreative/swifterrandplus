"""
Flask is a class that is used to instantiate web applications.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)


class User(db.Model, UserMixin):
    """Create a User table in the database."""
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password, date_created):
        """Initialize the User table."""
        self.username = username
        self.email = email
        self.password = password
        self.date_created = date_created


class SignupForm(FlaskForm):
    """Create a Sign-up form."""
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=4, max=15)],
        render_kw={"placeholder": "Username"}
    )
    email = StringField(
        'Email',
        validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=8, max=30)],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[InputRequired(), EqualTo('password')],
        render_kw={"placeholder": "Confirm Password"}
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate the user-name."""
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")


class LoginForm(FlaskForm):
    """Create a Login form."""
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=4, max=15)],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=8, max=30)],
        render_kw={"placeholder": "Password"}
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    """Return the login page."""
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/signup", strict_slashes=False, methods=["GET", "POST"])
def signup():
    """Return the signup page."""
    form = SignupForm()
    return render_template("signup.html", form=form)


@app.route("/user_dashboard", strict_slashes=False)
def user_dashboard():
    """Return the user to dashboard."""
    return render_template('user_dashboard.html')


@app.route("/logout", strict_slashes=False)
def logout():
    """Logout the user and clear session data."""
    session.pop('profile', None)
    return redirect(url_for('landing_page'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
