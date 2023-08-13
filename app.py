"""
Flask is a class that is used to instantiate web applications.
"""
import os
from flask import Flask, send_from_directory


# Path: app.py

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Great Minds!'

@app.route('/favicon.ico')
def favicon():
    """Return a favicon."""
    return send_from_directory(os.path.join(app.root_path, 'web_static', 'images'),
                               'icon_dark.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
