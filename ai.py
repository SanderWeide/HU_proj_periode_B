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


def sort_by_age_new():
    with open("temp.json") as f:
        temp = f.read()
    if temp != "":
        with open("temp.json") as f:
            data = json.load(f)
    else:
        with open("steam.json") as f:
            data = json.load(f)
    newlist = sorted(data, key=lambda d: d['release_date'], reverse=True)
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))
    f.close()

def sort_by_age_old():
    with open("temp.json") as f:
        temp = f.read()
    if temp != "":
        with open("temp.json") as f:
            data = json.load(f)
    else:
        with open("steam.json") as f:
            data = json.load(f)
    newlist = sorted(data, key=lambda d: d['release_date'])
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))
    f.close()

def sort_by_price_ascending():
    with open("temp.json") as f:
        temp = f.read()
    if temp != "":
        with open("temp.json") as f:
            data = json.load(f)
    else:
        with open("steam.json") as f:
            data = json.load(f)
    newlist = sorted(data, key=lambda d: d['price'])
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))
    f.close()

def sort_by_price_descending():
    with open("temp.json") as f:
        temp = f.read()
    if temp != "":
        with open("temp.json") as f:
            data = json.load(f)
    else:
        with open("steam.json") as f:
            data = json.load(f)
    newlist = sorted(data, key=lambda d: d['price'], reverse=True)
    f = open("temp.json", "w+")
    f.write(json.dumps(newlist))
    f.close()

def clean_temp():
    f = open("temp.json", "w").close()