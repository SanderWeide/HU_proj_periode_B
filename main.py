from GUI_dashboard import dashboard_gui
import json, threading, time
import ai
import random


random.seed()	
game = random.randrange(0,300)
print(game)

def start_gui():
        data = json.load(open("steam.json"))
        print(data[0])
        dashboard_gui.data_appid.config(text=data[game]['appid'])
        dashboard_gui.data_name.config(text=data[game]['name'])
        dashboard_gui.data_platforms.config(text=data[game]['platforms'])
        dashboard_gui.data_required_age.config(text=data[game]['required_age'])
        dashboard_gui.data_most_positive_ratings.config(text=ai.most_positive_reviews())
        dashboard_gui.data_review_ratio.config(text=ai.review_ratio())

start_gui()


dashboard_gui.window.mainloop()

