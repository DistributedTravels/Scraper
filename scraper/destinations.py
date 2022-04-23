import json

class Destinations:
    def __init__(self):
        self.destination = ""
        self.file_name = "destinations.json"

    def write_to_json_file(self):
        dictionary = {
            "destination": self.destination
        }
        json_object = json.dumps(dictionary, indent=1, ensure_ascii=False)
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(json_object)

