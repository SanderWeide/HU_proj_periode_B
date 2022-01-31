import json, threading, time
import re

data = json.load(open("steam.json"))

def mean(lst):
    return sum(lst)/len(lst)

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
    data = json.load(open("temp.json"))
    newlist = sorted(data, key=lambda d: d['release_date'])
    f = open("temp.json", "w+")
    f.write(newlist)

# def sort_by_age_old():
#     data = json.load(open("temp.json"))
#     newlist = sorted(data, key=lambda d: d['release_date'], reverse=True)
    
sort_by_age_new()


