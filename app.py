"""
Flask is a class that is used to instantiate web applications.
"""
from flask import Flask, render_template
from flask_fontawesome import FontAwesome


app = Flask(__name__)
fa = FontAwesome(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = 'static'


@app.route('/', strict_slashes=False)
def home_page():
    """Return the landing page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
