"""
Flask is a class that is used to instantiate web applications.
"""
import os
from flask import Flask, render_template


# Path: app.py

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """Return the landing page."""
    return render_template('index.html')


# @app.route('/favicon.ico', strict_slashes=False)
# def favicon():
#     """Return a favicon."""
#     return send_from_directory(
#         os.path.join(
#             app.root_path,
#             'static', 'images'
#         ),
#         'icon_dark.png', mimetype='image/png'
#     )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
