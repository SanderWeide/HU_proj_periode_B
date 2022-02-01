import json, threading, time
import re

data = json.load(open("steam.json"))

def mean(lst):
    return sum(lst)/len(lst)

def rnge(lst):
    low = min(lst)
    high = max(lst)
    return high - low

def var(lst):
    m = sum(lst) / len(lst)
    res = sum((i - m)**2 for i in lst) / len(lst)
    return res

selectie = []

for i in data:
    # print([i["name"], i["positive_ratings"]])
    selectie.append([i["name"], i["positive_ratings"]])
    
posRateSum = 0
for i in selectie:
    posRateSum += i[1]


def most_positive_reviews():
    most_positives = 0
    game_name = ""
    for i in data:
        if i["positive_ratings"] > most_positives:
            most_positives = i["positive_ratings"]
            game_name = i["name"]
    return game_name

def least_positive_reviews():
    most_negative = 0
    game_name = ""
    for i in data:
        if i["negative_ratings"] > most_negative:
            most_negative = i["negative_ratings"]
            game_name = i["name"]
    return game_name

def review_ratio():
    ratio = 0
    game_name = ""
    for i in data:
        if i["positive_ratings"] == 0 or i["negative_ratings"] == 0: continue
        if i["positive_ratings"] / i["negative_ratings"] > ratio:
            ratio = i["positive_ratings"] / i["negative_ratings"]
            game_name = i["name"]
    return game_name, ratio

def average_playtime():
    avg_playtime = 0
    game_name = ""
    for i in data:
        if i["average_playtime"] > avg_playtime:
            avg_playtime = i["average_playtime"]
            game_name = i["name"]
    return game_name, avg_playtime

def rating():
    rating_position = 0
    game_name = ""
    for i in data:
        if i["positive_ratings"] > rating_position:
            rating_position +1
            game_name = i["name"]
    return rating_position, game_name

def genre():
    game_genre = ""
    game_name = ""
    for i in data:
        if i["genres"] in data:
            game_genre = i["genres"]
            game_name = i["name"]
    return game_name, game_genre

def game_dev():
    developer = ""
    game_name = ""
    for i in data:
        if i["developer"] in data:
            developer = i["developer"]
            game_name = i["name"]
    return game_name, developer


def sort_by_age_new():
    data = json.load(open("temp.json"))
    newlist = sorted(data, key=lambda d: d['release_date'], reverse=True)
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))

def sort_by_age_old():
    data = json.load(open("temp.json"))
    newlist = sorted(data, key=lambda d: d['release_date'])
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))

def sort_by_price_ascending():
    data = json.load(open("temp.json"))
    newlist = sorted(data, key=lambda d: d['price'])
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))

def sort_by_price_descending():
    data = json.load(open("temp.json"))
    newlist = sorted(data, key=lambda d: d['price'], reverse=True)
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))

