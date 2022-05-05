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
    

dest = [a['arrival'] if a['hotel'] != "" else "" for a in offers]
final_dest = set()
for i in dest:
    tmp = i.split('\\')
    tmp = tmp[0].split('-')
    a = ""
    for t in tmp:
        a += t.capitalize() + " "
    final_dest.add(a.strip())
    
final_dest.remove("")
final_dest.remove("Wlochy")
final_dest.add("Włochy")
final_dest.remove("Czarnogora")
final_dest.add("Czarnogóra")
final_dest.remove("Bulgaria")
final_dest.add("Bułgaria")
final_dest.remove("Wyspy Zielonego Przyladka")
final_dest.add("Wyspy Zielonego Przylądka")

with open('dest.json', 'w', encoding='utf-8') as f:
    final_dest = list(final_dest)
    final_dest.sort()
    json.dump(final_dest, f, ensure_ascii=False)

hotels = [
    [a['hotel'], 
     a['arrival'].replace("wlochy", "włochy").replace("czarnogora", "czarnogóra").replace("bulgaria", "bułgaria").replace("wyspy-zielonego-przyladka", "wyspy-zielonego-przylądka")
     ] if a['hotel'] != "" else "" for a in offers]
hotels = list(filter(lambda a: a != "", hotels))
final_hotel = set()
for i in hotels:
    a = ""
    tmp = str.split(i[0], '-')
    for t in tmp:
        a += t.capitalize() + " "
    tmp = i[1].split('\\')
    tmp = tmp[0].split('-')
    b = ""
    for t in tmp:
        b += t.capitalize() + " "
    
    final_hotel.add((a.strip(), b.strip()))

with open('hotels.json', 'w', encoding='utf-8') as f:
    final_hotels = list(final_hotel)
    final_hotels.sort()
    json.dump(final_hotels, f, ensure_ascii=False)
