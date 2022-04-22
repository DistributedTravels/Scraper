import re
import json
import bs4

class Offers:
    def __init__(self, offer : bs4.element.Tag, departure, room, transport):
        self.offer = offer
        self.hotel = self.get_hotel()
        self.stars = self.get_stars()
        self.price = self.get_price()
        self.departure = departure
        self.arrival = self.get_arrival()
        self.trip = self.get_trip()
        self.room = room
        self.transport = transport
        self.file_name = "offers.json"

    def get_stars(self):
        try:
            return float(self.offer.find('span', class_='hotel-rank').get_text())
        except AttributeError:
            return 0

    def get_price(self):
        try:
            price = self.offer.find('span', class_='current-price_value').get_text()
            return int(re.findall(r'(.*)PLN \/ os', price)[0].replace(" ", ""))
        except Exception as e:
            print(e)
            return None

    def get_hotel(self):
        link = self.offer.find('a', {'class': 'offer_link pull-right'}).get('href')

        part = link.split('/')
        for p in part:
            if p.startswith('hotel') and (',' in p):
                list = p.split(',')
                return list[0]
        return ""

    def get_arrival(self):
        link = self.offer.find('a', {'class': 'offer_link pull-right'}).get('href')
        part = link.split('/')

        if not part[3].startswith('hotel'):
            if ',' in part[3]:
                list = part[3].split(',')
                return part[2] + "\\" + list[0]
            return part[2] + "\\" + part[3]

        return part[2]

    def get_trip(self):
        link = self.offer.find('a', {'class': 'offer_link pull-right'}).get('href')
        part = link.split('/')
        return part[1]



    def write_to_json_file(self):
        dictionary = {
            "hotel": self.hotel,
            "stars": self.stars,
            "price": self.price,
            "departure": self.departure,
            "arrival": self.arrival,
            "trip": self.trip,
            "room": self.room,
            "transport": self.transport
        }
        json_object = json.dumps(dictionary, indent=1)
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(json_object)


