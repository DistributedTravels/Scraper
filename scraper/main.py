import sys
from scrapper import Scrapper

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to specify single path argument")
        exit(1)

    url = sys.argv[1]
    scrapper = Scrapper(url)
    scrapper.get_destinations()
    scrapper.get_offers()
    scrapper.get_trips()

