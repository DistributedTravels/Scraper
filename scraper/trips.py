import json
import bs4

class Trips:
    def __init__(self, t : bs4.element.Tag):
        self.t = t
        self.trip = self.get_trip()
        self.file_name = "trips.json"

    def write_to_json_file(self):
        dictionary = {
            "trip": self.trip
        }
        json_object = json.dumps(dictionary, indent=1)
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(json_object)

    def get_trip(self):
        trip = self.t.get_text()
        trip = trip.strip('\n')
        return trip
