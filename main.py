from GUI_dashboard import dashboard_gui
import json, threading, time, random, ai
import search
random.seed()


def game_genres_filter():
    active_filters = []
    if dashboard_gui.Free_to_Play_option.get():
        active_filters.append("Free to Play")
    if dashboard_gui.Early_Access_option.get():
        active_filters.append("Early Access")
    if dashboard_gui.Action_option.get():
        active_filters.append("Action")
    if dashboard_gui.Advanture_option.get():
        active_filters.append("Advanture")
    if dashboard_gui.Casual_option.get():
        active_filters.append("Casual")
    if dashboard_gui.Indie_option.get():
        active_filters.append("Indie")
    if dashboard_gui.Massively_Multiplayer_option.get():
        active_filters.append("Massively Multiplayer")
    if dashboard_gui.Racing_option.get():
        active_filters.append("Racing")
    if dashboard_gui.RPG_option.get():
        active_filters.append("RPG")
    if dashboard_gui.Simulation_option.get():
        active_filters.append("Simulation")
    if dashboard_gui.Sports_option.get():
        active_filters.append("Sports")
    if dashboard_gui.Strategy_option.get():
        active_filters.append("Strategy")
    search.search(active_filters)


data = json.load(open("steam.json"))
dashboard_gui.button_apply_filter.config(command = game_genres_filter)

dashboard_gui.window.mainloop()

def sort_filter():
    selection = dashboard_gui.value_option_menu.get()
    if selection == "Date  (new - old)":
        print("new old")
    if selection == "Date  (old - new)":
        print("old new")
    if selection == "Price (ascending)":
        print("price asc")
    if selection == "Price (descending)":
        print("price des")

