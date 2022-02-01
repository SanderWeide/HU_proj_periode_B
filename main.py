from GUI_dashboard import dashboard_gui
import json, threading, time, random, ai, search
from pathlib import Path
random.seed()

def sort_filter():
    selection = dashboard_gui.value_option_menu.get()
    if selection == "Date  (new - old)":
        ai.sort_by_age_new()
    if selection == "Date  (old - new)":
        ai.sort_by_age_old()
    if selection == "Price (ascending)":
        ai.sort_by_price_ascending()
    if selection == "Price (descending)":
        ai.sort_by_price_descending()

def game_genres_filter():
    active_filters = []
    price_range = dashboard_gui.value_price_menu.get()
   
    
    #catagory filter
    if dashboard_gui.Free_to_Play_option.get():
        active_filters.append("Free to Play")
    if dashboard_gui.Early_Access_option.get():
        active_filters.append("Early Access")
    if dashboard_gui.Action_option.get():
        active_filters.append("Action")
    if dashboard_gui.Adventure_option.get():
        active_filters.append("Adventure")
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
     # price filter
    if price_range == "Games under €5":
        active_filters.append("under5")
    if price_range == "Games under €10":
        active_filters.append("under10")
    if price_range == "Games under €20":
        active_filters.append("under20")
    if price_range == "Games under €40":
        active_filters.append("under40")
    if price_range == "Games over €40":
        active_filters.append("over40")
        
    search.search(active_filters)



data = json.load(open("steam.json"))
dashboard_gui.button_apply_filter.config(command = game_genres_filter)

dashboard_gui.button_apply_sort.config(command = sort_filter)


dashboard_gui.window.mainloop()



