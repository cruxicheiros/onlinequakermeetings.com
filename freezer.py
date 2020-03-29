from flask_frozen import Freezer
from application import create_app
import os

app = create_app()
app.config["FREEZER_RELATIVE_URLS"] = True
freezer = Freezer(create_app())

if __name__ == '__main__':
    freezer.freeze()