import json

offers = []
with open("scraper\offers.json", 'r', encoding='utf-8') as f:
    tmp = f.read()
    tmp = tmp.split("}")
    tmp = [e+'}' for e in tmp]
    tmp2 = []
    for obj in tmp[:-1]:
        obj = obj.split('\n')
        tmp2.append("".join(obj))
    for jsonStr in tmp2:
        offers.append(json.loads(jsonStr))
    
sources = [a['departure'] for a in offers]
final_sources = set()
for i in sources:
    tmp = i.split('\\')
    for s in tmp:
        final_sources.add(s)

final_sources.remove('')
final_sources.remove('Warszawa - Modlin')
final_sources.remove('Bielsko - Biała')
final_sources.add('Bielsko-Biała')
final_sources.remove('Dojazd własny')

final_sources.difference_update(['Augustów', 'Gorzów Wielkopolski', "Grajewo", "Głubczyce", "Gliwice", "Legnica", "Leszno", "Piotrków Trybunalski", "Piła", "Suwałki", "Szczuczyn", "Słupsk", "Torzym", "Zgorzelec", "Zielona Góra", "Łomża", "Białystok", "Bielsko-Biała", "Ełk", "Częstochowa", "Koszalin", "Opole", "Toruń"])

final_sources = list(final_sources)
final_sources.sort()

with open('sources.json', 'w', encoding='utf-8') as f:
    json.dump(final_sources, f, ensure_ascii=False)
