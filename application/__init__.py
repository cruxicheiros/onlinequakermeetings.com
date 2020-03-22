import os
from flask import Flask, render_template
from iso3166 import countries
from .meetings import MeetingCollection, CategoryCollection, Category

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MEETINGS_CSV=os.path.join(app.root_path, 'meetings.csv')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Load all meetings from csv
    meeting_collection = MeetingCollection()
    meeting_collection.import_csv(app.config['MEETINGS_CSV'])

    # the homepage
    @app.route('/')
    def index():
        meetings_by_country = meeting_collection.split_by_country()
        categories = CategoryCollection()

        for country_code, meetings in meetings_by_country.items():
            country_name = countries.get(country_code).name
            new_category = Category(country_name, meetings.sort_by_name())
            categories.add(new_category)

        sorted_categories = categories.sort_by_name()

        return render_template("index.html", categories=sorted_categories)

    return app