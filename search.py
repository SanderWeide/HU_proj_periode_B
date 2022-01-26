import json

def search(active_filters):
    temp = []
    data = json.load(open("steam.json"))
    for i in data:
        if "Free to Play" in active_filters:
            if "Free to Play" not in i["genres"]:
                continue
        if "Early Access" in active_filters:
            if "Early Access" not in i["genres"]:
                continue
        if "Action" in active_filters:
            if "Action" not in i["genres"]:
                continue
        if "Advanture" in active_filters:
            if "Advanture" not in i["genres"]:
                continue
        if "Casual" in active_filters:
            if "Casual" not in i["genres"]:
                continue
        if "Indie" in active_filters:
            if "Indie" not in i["genres"]:
                continue
        if "Massively Multiplayer" in active_filters:
            if "Massively Multiplayer" not in i["genres"]:
                continue
        if "Racing" in active_filters:
            if "Racing" not in i["genres"]:
                continue
        if "RPG" in active_filters:
            if "RPG" not in i["genres"]:
                continue
        if "Simulation" in active_filters:
            if "Simulation" not in i["genres"]:
                continue
        if "Sports" in active_filters:
            if "Sports" not in i["genres"]:
                continue
        if "Strategy" in active_filters:
            if "Strategy" not in i["genres"]:
                continue
        temp.append(i)
        print(temp)