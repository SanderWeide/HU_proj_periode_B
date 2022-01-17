from GUI_dashboard import dashboard_gui
import json, threading, time

def start_gui():
        data = json.load(open("steam.json"))
        print(data[0])
        dashboard_gui.data_appid.config(text=data[0]['appid'])
        dashboard_gui.data_name.config(text=data[0]['name'])
        dashboard_gui.data_platforms.config(text=data[0]['platforms'])
        dashboard_gui.data_required_age.config(text=data[0]['required_age'])
        dashboard_gui.data_positive_ratings.config(text=data[0]['positive_ratings'])

start_gui()


dashboard_gui.window.mainloop()

