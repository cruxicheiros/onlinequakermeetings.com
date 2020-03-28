# Simple wrapper for iso3166.countries
# allowing customisation of country names and referring to countries as objects

import iso3166

class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return "Country(code={self.code}, name={self.name})".format(self=self)

class CountryRepository:
    def __init__(self):
        self.custom_names = {"gb" : "United Kingdom"}

    def get(self, keyword):        
        fetched_country = iso3166.countries.get(keyword.upper())
        country_code = fetched_country.alpha2.lower()

        print(country_code)

        if country_code in self.custom_names:
            country_name = self.custom_names[country_code]
        else:
            country_name = fetched_country.name
        
        print(country_name)

        return Country(country_code, country_name)