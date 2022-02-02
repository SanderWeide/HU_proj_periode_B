import json
import ai
import search


from GUI_dashboard import dashboard_gui
from tkinter import END

show_games_min = 0
show_games_max = 12

with open("steam.json") as f:
    data = json.load(f)

ai.clean_temp()

filteredData = data

def get_game_name(appid):
    with open("steam.json") as f:
        data = json.load(f)
    for i in data:
        if i["appid"] == appid:
            return i["name"]
    
    return "NO GAME NAME FOUND"


def get_achievements(appid):
    with open("steam.json") as f:
        data = json.load(f)
    for i in data:
        if i["appid"] == appid:
            return i["name"]
    
    return "NO GAME NAME FOUND"

def get_postive_ratings(appid):
    with open("steam.json") as f:
        data = json.load(f)
    for i in data:
        if i["appid"] == appid:
            return i["positive_ratings"]
    
    return "NO RATING FOUND"

def get_negative_ratings(appid):
    with open("steam.json") as f:
        data = json.load(f)
    for i in data:
        if i["appid"] == appid:
            return i["negative_ratings"]
    
    return "NO RATING FOUND"

def get_review_ratio(appid):
    with open("steam.json") as f:
        data = json.load(f)
    for i in data:
        if i["appid"] == appid:
            return i["negative_ratings"]
    
    return "NO RATING FOUND"



def back_to_gamelist():
    dashboard_gui.destroy_game_info_page()
    dashboard_gui.homescreen()
    with open("temp.json") as f:
        temp = f.read()
    if temp == "":
        game_info_button_command(data[show_games_min:show_games_max])
    else:
        with open("temp.json") as f:
            skrt = json.load(f)
        game_info_button_command(skrt[show_games_min:show_games_max])
    return

def game_stats(appid):
    dashboard_gui.destroy_homescreen()
    dashboard_gui.destroy_games()
    game_name = get_game_name(appid)
    dashboard_gui.back_button.config(command=back_to_gamelist)
    dashboard_gui.game_info_page(appid, game_name)

def game_info_button_command(data):
    try:
        dashboard_gui.destroy_games()
    except: None
    dashboard_gui.show_games(data)
    dashboard_gui.button_open_game1.config(command= lambda: game_stats(data[0]["appid"]))
    dashboard_gui.button_open_game2.config(command= lambda: game_stats(data[1]["appid"]))
    dashboard_gui.button_open_game3.config(command= lambda: game_stats(data[2]["appid"]))
    dashboard_gui.button_open_game4.config(command= lambda: game_stats(data[3]["appid"]))
    dashboard_gui.button_open_game5.config(command= lambda: game_stats(data[4]["appid"]))
    dashboard_gui.button_open_game6.config(command= lambda: game_stats(data[5]["appid"]))
    dashboard_gui.button_open_game7.config(command= lambda: game_stats(data[6]["appid"]))
    dashboard_gui.button_open_game8.config(command= lambda: game_stats(data[7]["appid"]))
    dashboard_gui.button_open_game9.config(command= lambda: game_stats(data[8]["appid"]))
    dashboard_gui.button_open_game10.config(command= lambda: game_stats(data[9]["appid"]))
    dashboard_gui.button_open_game11.config(command= lambda: game_stats(data[10]["appid"]))
    dashboard_gui.button_open_game12.config(command= lambda: game_stats(data[11]["appid"]))




def GetNameParts() -> list[str]:
    name: str = dashboard_gui.searchBox.get("1.0", END)
    name = name.strip()
    nameParts = name.split(' ')

    return nameParts

def sort_filter():
    global show_games_max
    global show_games_min
    selection = dashboard_gui.value_option_menu.get()
    if selection == "Date  (new - old)":
        ai.sort_by_age_new()
    if selection == "Date  (old - new)":
        ai.sort_by_age_old()
    if selection == "Price (ascending)":
        ai.sort_by_price_ascending()
    if selection == "Price (descending)":
        ai.sort_by_price_descending()

    show_games_min = 0
    show_games_max = 12
    with open("temp.json") as f:
        temp = f.read()
    if temp != "":
        with open("temp.json") as f:
            skrt = json.load(f)
    else:
        with open("steam.json") as f:
            skrt = json.load(f)
    game_info_button_command(skrt[show_games_min:show_games_max])


PriceRangeOptions = {
    "Games under €5": 5,
    "Games under €10": 10,
    "Games under €20": 20,
    "Games under €40": 40
}

def game_genres_filter():
    global filteredData
    global show_games_max
    global show_games_min
    filteredData = data

    active_filters = []

    price_range = dashboard_gui.value_price_menu.get()
    nameParts = GetNameParts()

    # catagory filter
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
    if price_range in PriceRangeOptions:
        filteredData = search.ApplyPriceFilter(filteredData, 0, PriceRangeOptions[price_range])

    if len(nameParts) > 0:
        filteredData = search.ApplyNameFileter(filteredData, nameParts)

    if len(active_filters) > 0:
        filteredData = search.ApplyGenreFilter(filteredData, active_filters)

    

    f = open("temp.json", "w+")
    f.write(json.dumps(filteredData))
    f.close()
    show_games_min = 0
    show_games_max = 12
    game_info_button_command(filteredData[show_games_min:show_games_max])
    sort_filter()


dashboard_gui.homescreen()
game_info_button_command(data[show_games_min:show_games_max])
dashboard_gui.button_apply_filter.config(command=game_genres_filter)
dashboard_gui.searchButton.config(command=game_genres_filter)
dashboard_gui.button_apply_sort.config(command = game_genres_filter)
def show_games_next():
    global show_games_min
    global show_games_max
    show_games_min += 12
    show_games_max += 12
    dashboard_gui.destroy_games()
    with open("temp.json") as f:
        temp = f.read()
    if temp == "":
        game_info_button_command(data[show_games_min:show_games_max])
    else:
        with open("temp.json") as f:
            skrt = json.load(f)
        game_info_button_command(skrt[show_games_min:show_games_max])

def show_games_back():
    global show_games_min
    global show_games_max
    if show_games_max <= 12:
        return
    
    show_games_min -= 12
    show_games_max -= 12
    dashboard_gui.destroy_games()
    with open("temp.json") as f:
        temp = f.read()
    if temp == "":
        game_info_button_command(data[show_games_min:show_games_max])
    else:
        with open("temp.json") as f:
            skrt = json.load(f)
        game_info_button_command(skrt[show_games_min:show_games_max])

dashboard_gui.button_forward.config(command = show_games_next)
dashboard_gui.button_back.config(command = show_games_back)
dashboard_gui.window.mainloop()



