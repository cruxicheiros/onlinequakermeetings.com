import csv

class Meeting:
    def __init__(self, name, **kwargs):
        self.name = name
        self.metadata = kwargs

class MeetingCollection:
    def __init__(self, meetings=None):
        if meetings == None:
            self.meetings = []
        else:
            self.meetings = meetings

    def import_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:

                meeting = Meeting(
                    row['NAME'],
                    country=row['COUNTRY'],
                    state_province=row['STATE_PROVINCE'],
                    city_town=row['CITY_TOWN'],
                    link=row['LINK'],
                    worship_format=row['WORSHIP_FORMAT'],
                    medium=row['MEDIUM'],
                    medium_format=row['MEDIUM_FORMAT'].strip('"'),
                    is_live=int(row['IS_LIVE'])
                )

                self.meetings.append(meeting)

    def add(self, meeting):
        self.meetings.append(meeting)
    
    # ISO two-character codes
    def filter_by_country(self, country_code):
        meetings_by_country = [m for m in self.meetings if (meeting.metadata["country"] == country_code)]
        return MeetingCollection(meetings_by_country)

    def split_by_country(self):
        country_groups = {}
        
        for meeting in self.meetings:
            if meeting.metadata["country"] in country_groups:
                country_groups[meeting.metadata["country"]].add(meeting)
            else:
                country_groups[meeting.metadata["country"]] = MeetingCollection([meeting])
        
        return country_groups

    def to_list(self):
        return self.meetings

    def sort_by_name(self, reverse=False):
        sorted_meetings = self.meetings.copy()
        sorted_meetings.sort(key=lambda x: x.name, reverse=reverse)

        return MeetingCollection(sorted_meetings)

class Category:
    def __init__(self, name, meetings):
        self.name = name
        self.meetings = meetings

class CategoryCollection:
    def __init__(self, categories=None):
        if categories == None:
            self.categories = []
        else:
            self.categories = categories

    def to_list(self):
        return self.categories

    def add(self, category):
        self.categories.append(category)

    def sort_by_name(self, reverse=False):
        sorted_categories = self.categories.copy()
        sorted_categories.sort(key=lambda x: x.name, reverse=reverse)

        return CategoryCollection(sorted_categories)
    
