import json

def search(active_filters):
    temp = ""
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
        if "Adventure" in active_filters:
            if "Adventure" not in i["genres"]:
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
        if "under5" in active_filters:
            if i["price"] > 5:
                continue
        if "under10" in active_filters:
            if i["price"] > 10:
                continue
        if "under20" in active_filters:
            if i["price"] > 20:
                continue
        if "under40" in active_filters:
            if i["price"] > 40:
                continue
        if "over40" in active_filters:
            if i["price"] <= 40:
                continue
        temp += str(i)
    temp = temp.replace("}{","}, {")
    temp = temp.replace("\'", "\"")
    temp = "[" + temp + "]"
    f = open("temp.json", "w+")
    f.write(temp)

# def sort_json():
#     if 

# def search_bar():
#     data = json.load(open("steam.json"))
#     if data == "":
       
#     for i in data: 
#         if "Free to Play" in active_filters:
#             if "Free to Play" not in i["genres"]:
#                 continue