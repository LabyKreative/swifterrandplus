"""This module contains the main application code for the Flask app.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from flask_dance.contrib.google import make_google_blueprint, google
from flask_fontawesome import FontAwesome

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]
oauth = OAuth(app)

hate_you_majay = os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)

# Configure Google OAuth
google_bp = make_google_blueprint(
    client_id=os.environ['GOOGLE_CLIENT_ID'],
    client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    redirect_to='google.login'
)
app.register_blueprint(google_bp, url_prefix="/google_login")


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login")
def login():
    """Initiate the Google OAuth login process."""
    if not google.authorized:
        return render_template("login.html")
    else:
        return redirect(url_for('user_dashboard'))


@app.route("/user_dashboard")
def user_dashboard():
    """Return the user's dashboard after successful login."""
    if not google.authorized:
        # If not authorized, redirect to the login page
        return redirect(url_for('login'))
    # Get user info from the OAuth provider (Google in this case)
    resp = google.get('/userinfo')
    user_info = resp.json()
    # You can store the user_info in the session or use it as needed
    session['user_info'] = user_info
    # Render the user dashboard template
    return render_template('user_dashboard.html')


@app.route("/logout", strict_slashes=False)
def logout():
    """Logout the user and clear session data."""
    session.pop('google_oauth_token', None)
    return redirect(url_for("landing_page"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
