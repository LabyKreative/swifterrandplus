"""
Flask is a class that is used to instantiate web applications.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, session, request
# from flask_oauthlib.client import OAuth
from flask_fontawesome import FontAwesome


load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)


# Configuration for Google OAuth
# oauth = OAuth(app)

# google = oauth.remote_app(
#     'google',
#     consumer_key='your_google_client_id',
#     consumer_secret='your_google_client_secret',
#     request_token_params={
#         'scope': 'email',
#     },
#     base_url='https://www.googleapis.com/oauth2/v1/',
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
# )


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page with a sign-in button."""
    return render_template("index.html")


@app.route("/login")
def login():
    """Initiate the Google OAuth login process."""
    return render_template("login.html")
    # return google.authorize(callback=url_for('authorized', _external=True))


# @app.route("/logout")
# def logout():
#     """Logout the user and clear session data."""
#     session.pop('google_token', None)
#     return redirect(url_for('landing_page'))


# @app.route("/login/authorized")
# def authorized():
#     """Callback after successful Google OAuth authorization."""
#     response = google.authorized_response()
#     if response is None or response.get('access_token') is None:
#         return "Access denied: reason={} error={}".format(
#             request.args['error_reason'],
#             request.args['error_description']
#         )

#     session['google_token'] = (response['access_token'], '')
#     user_info = google.get('userinfo')

#     # Store or use user_info as needed

#     return redirect(url_for('user_dashboard'))

# @google.tokengetter
# def get_google_oauth_token():
#     return session.get('google_token')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
