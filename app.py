"""
Flask is a class that is used to instantiate web applications.
"""
import os
from flask import request
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from flask_fontawesome import FontAwesome

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)


# OAuth Config
oauth = OAuth(app)
google = oauth.register(
    name='swifterrandplus',
    client_id=os.environ['GOOGLE_CLIENT_ID'],
    client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=os.environ['GOOGLE_META_URL'],
)


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login")
def login():
    """Initiate the Google OAuth login process."""
    google = oauth.create_client('swifterrandplus')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/authorize", strict_slashes=False)
def authorized():
    """Callback after successful Google OAuth authorization."""
    token = google = oauth.create_client('swifterrandplus')
    user_info = google.parse_id_token(token, nonce=session['nonce'])
    # Store user information in the sessio
    session['profile'] = user_info
    session.permanent = True
    return redirect(url_for('user_dashboard'))


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
