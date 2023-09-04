"""
Flask is a class that is used to instantiate web applications.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session
from flask_fontawesome import FontAwesome

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login", strict_slashes=False)
def login():
    """Return the login page."""
    return render_template("login.html")


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
