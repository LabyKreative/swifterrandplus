"""
Flask is a class that is used to instantiate web applications.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/', strict_slashes=False)
def home_page():
    """Return the landing page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
