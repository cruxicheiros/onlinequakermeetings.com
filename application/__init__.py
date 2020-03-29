import os
from flask import Flask, render_template, abort
from .countries import CountryRepository
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

    # Initialise country repository
    countries = CountryRepository()

    # the homepage
    @app.route('/')
    def index():
        return render_template("index.html")

    # Directory page
    @app.route('/directory')
    def directory():
        meetings_by_country = meeting_collection.split_by_country()
        categories = CategoryCollection()

        for country_code, meetings in meetings_by_country.items():
            country = countries.get(country_code)
            new_category = Category(country.name, meetings.sort_by_name())
            categories.add(new_category)

        sorted_categories = categories.sort_by_name()

        return render_template("/directory/index.html", categories=sorted_categories)

    # Define list of countries with specific information for finding meetings
    specific_info_country_codes = ["au", "gb", "us"]
    specific_info_countries = [countries.get(code) for code in specific_info_country_codes]

    # 'how to find your meeting' page
    @app.route('/findmeetings')
    def find_your_meeting():
        return render_template("find_a_meeting/index.html", countries=specific_info_countries)

    @app.route('/findmeetings/<country_code>')
    def find_meeting_country_info(country_code):
        if country_code in specific_info_country_codes:
            country = countries.get(country_code)
            return render_template("find_a_meeting/country_specific/" + country.code + "/index.html", country=country)
        else:
            abort(404)

    return app