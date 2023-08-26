"""
Flask is a class that is used to instantiate web applications.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_fontawesome import FontAwesome


load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = "static"
fa = FontAwesome(app)


@app.route("/", strict_slashes=False)
def landing_page():
    """Return the landing page."""
    return render_template("base.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
