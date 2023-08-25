"""
Flask is a class that is used to instantiate web applications.
"""
import os
from flask import Flask, render_template, url_for, redirect, session
from flask_fontawesome import FontAwesome
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    client_kwargs={"scope": "openid email profile"},
)
fa = FontAwesome(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"


@app.route("/", strict_slashes=False)
def home_page():
    """Return the landing page."""
    return render_template("base.html")


@app.route("/login")
def login():
    """Return the login page."""
    google = oauth.create_client("google")
    redirect_uri = url_for("authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/authorize")
def authorize():
    """Return the authorize page."""
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    resp = google.get("userinfo", token=token)
    user_info = resp.json()
    # user = oauth.google.userinfo()
    session["user_email"] = user_info["email"]
    session.permanent = True
    # do something with the token and profile
    return redirect("/")


@app.route("/logout")
def logout():
    """Logout the user."""
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
