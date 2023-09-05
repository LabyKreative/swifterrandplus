"""
Flask is a class that is used to instantiate web applications.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
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


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login", strict_slashes=False)
def login():
    """Return the login page."""
    return render_template("login.html")


@app.route("/signup", strict_slashes=False)
def signup():
    """Return the signup page."""
    return render_template("signup.html")


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
