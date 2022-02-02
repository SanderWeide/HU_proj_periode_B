from pathlib import Path
from tkinter import *
import json
from turtle import clear
from GUI_dashboard import apihelper

variableHeight = 35
relativeYPost = 35
YTopMargin = 120

value_option_menu = ""
# variableHeight voor de hoogte van de items
# relativeYPost*0+YTopMargin voor y positie, pas de 0 aan naar het hoeveelste item het is

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title('Steam Dashboard')
window.geometry("1280x720")
# window.configure(bg = "#2a475e")


canvas = Canvas(
    window,
    bg = "#2a475e",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    )

canvas.place(x = 0, y = 0)

img = PhotoImage(file=relative_to_assets("page_bg_generated_v6b.png")),
steam_background = canvas.create_image(
    600,
    400,
    image=img
)


steamlogo = PhotoImage(
    file=relative_to_assets("steam_resize.png"))
steam_logo = canvas.create_image(
    60,
    60,
    image=steamlogo
)


# selectie menu sorteer opties
options = [
    'Sort By',
    'Date  (new - old)',
    'Date  (old - new)',
    'Price (ascending)',
    'Price (descending)']

value_option_menu = StringVar(window)
value_option_menu.set(options[0]) # default value
filter_selection_menu = OptionMenu(window, value_option_menu, *options,)


#Price options
label_price_options = Label(window, 
    text="Game category",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)

#backwords button
button_back = Button(window, 
    text="<-- Back",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")
    
#forward button
button_forward = Button(window, 
    text="Next -->",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

# game list header
label_name0 = Label(window, 
    text="Name:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)

label_platform0 = Label(window, 
    text="Platform:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)

label_release0 = Label(window, 
    text="Date:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)

label_price0 = Label(window, 
    text="Price:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)

label_info0 = Label(window, 
    text="Info:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)

# filter opties
Free_to_Play_option = IntVar()
checkbutton_free_to_play = Checkbutton(window, text="Free to Play", variable=Free_to_Play_option)
Early_Access_option = IntVar()
checkbutton_early_access_option = Checkbutton(window, text="Early Access", variable=Early_Access_option)
Action_option = IntVar()
checkbutton_action_option = Checkbutton(window, text="Action", variable=Action_option)
Adventure_option = IntVar()
checkbutton_adventure_option = Checkbutton(window, text="Adventure", variable=Adventure_option)
Casual_option = IntVar()
checkbutton_casual_option = Checkbutton(window, text="Casual", variable=Casual_option)
Indie_option = IntVar()
checkbutton_indie_option = Checkbutton(window, text="Indie", variable=Indie_option)
Massively_Multiplayer_option = IntVar()
checkbutton_massively_multiplayer_option = Checkbutton(window, text="Massively Multiplayer", variable=Massively_Multiplayer_option)
Racing_option = IntVar()
checkbutton_racing_option = Checkbutton(window, text="Racing", variable=Racing_option)
RPG_option = IntVar()
checkbutton_RPG_option = Checkbutton(window, text="RPG", variable=RPG_option)
Simulation_option = IntVar()
checkbutton_simulation_option = Checkbutton(window, text="Simulation", variable=Simulation_option)
Sports_option = IntVar()
checkbutton_sports_option = Checkbutton(window, text="Sports", variable=Sports_option)
Strategy_option = IntVar()
checkbutton_strategy_option = Checkbutton(window, text="Strategy", variable=Strategy_option)

#Price options
label_filter_apply = Label(window, 
    text="Price category",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)

#prijs filter menu
price_options = [
    'Select price range',
    'Games under €5',
    'Games under €10',
    'Games under €20',
    'Games under €40',
    'Games over €40']

value_price_menu = StringVar(window)
value_price_menu.set(price_options[0]) # default value

price_filter_menu = OptionMenu(window, value_price_menu, *price_options,)


# searchbox
searchBox = Text(window,
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12")

# searchbutton
searchButton = Button (window, text="Zoeken")

# sort menu apply knop
button_apply_sort = Button(window, 
    text="Sort",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold"
    )

#Filter apply knop
button_apply_filter = Button(window, 
    text="Apply Filter",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)


# TI SnackBox controle knoppen
UnlockSnackBoxButton = Button(window, text="Ontgrendel SnackDoos")
LockSnackBoxButton = Button(window, text="Vergrendel SnackDoos")



def homescreen():
    # TI SnackBox controle knoppen
    UnlockSnackBoxButton.place(x=1100.0, y=25.0, width=160, height=25)
    LockSnackBoxButton.place(x=1100.0, y=55.0, width=160, height=25)
    # searchbox
    searchBox.place(
        x=200,
        y=25,
        width=540,
        height=25)


    # searchbutton
    searchButton.place(
        x=740,
        y=25,
        width=60,
        height=25)

    # filter
    # filter_selectie(options)

    # sort menu apply knop
    button_apply_sort.place(x=1015,
    y=25.0,
    width=50,
    height=25)

    #Filter apply knop
    button_apply_filter.place(x=20.0,
    y=120.0,
    width=160,
    height=25)


    #Price options
    label_price_options.place(x=20.0,y=155.0,width=160,height=25)

    # filter opties
    checkbutton_free_to_play.place(x=20.0,y=180.0,width=160,height=25)
    checkbutton_early_access_option.place(x=20.0,y=200.0,width=160,height=25)
    checkbutton_action_option.place(x=20.0,y=220.0,width=160,height=25)
    checkbutton_adventure_option.place(x=20.0,y=240.0,width=160,height=25)
    checkbutton_casual_option.place(x=20.0,y=260.0,width=160,height=25)
    checkbutton_indie_option.place(x=20.0,y=280.0,width=160,height=25)
    checkbutton_massively_multiplayer_option.place(x=20.0,y=300.0,width=160,height=25)
    checkbutton_racing_option.place(x=20.0,y=320.0,width=160,height=25)
    checkbutton_RPG_option.place(x=20.0,y=340.0,width=160,height=25)
    checkbutton_simulation_option.place(x=20.0,y=360.0,width=160,height=25)
    checkbutton_sports_option.place(x=20.0,y=380.0,width=160,height=25)
    checkbutton_strategy_option.place(x=20.0,y=400.0,width=160,height=25)

    #Price options
    label_filter_apply.place(x=20.0,y=435.0,width=160,height=25)

    #prijs filter menu
    price_filter_menu.place(
        x=20.0,
        y=460.0,
        width=160,
        height=25
    )


    filter_selection_menu.place(
        x=850.0,
        y=25.0,
        width=160,
        height=25
    )

    #backwords button
    button_back.place(x=300.0,y=650.0,width=160,height=25)


    #forward button
    button_forward.place(x=800.0,y=650.0,width=160,height=25)

    # game list header
    label_name0.place(
        x=200,
        y=relativeYPost*0+YTopMargin,
        width=450,
        height=variableHeight)

    label_platform0.place(
        x=650,
        y=relativeYPost*0+YTopMargin,
        width=200,
        height=variableHeight)

    label_release0.place(
        x=850,
        y=relativeYPost*0+YTopMargin,
        width=100,
        height=variableHeight)

    label_price0.place(
        x=950,
        y=relativeYPost*0+YTopMargin,
        width=65,
        height=variableHeight)

    label_info0.place(
        x=1015,
        y=relativeYPost*0+YTopMargin,
        width=50,
        height=variableHeight)


def show_games(gameData):
        for i in range(1,13): 
            if i % 2:
                globals()[f"label_name{i}"] = Label(window, 
                    text=gameData[i-1]["name"],
                    fg = "#c7d5e0",
                    bg = "#313d4b",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_name{i}"].place(
                    x=200,
                    y=relativeYPost*i+YTopMargin,
                    width=450,
                    height=variableHeight)

                globals()[f"label_platform{i}"] = Label(window, 
                    text=gameData[i-1]["platforms"],
                    fg = "#c7d5e0",
                    bg = "#313d4b",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_platform{i}"].place(
                    x=650,
                    y=relativeYPost*i+YTopMargin,
                    width=200,
                    height=variableHeight)

                globals()[f"label_release{i}"] = Label(window, 
                    text=gameData[i-1]["release_date"],
                    fg = "#c7d5e0",
                    bg = "#313d4b",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_release{i}"].place(
                    x=850,
                    y=relativeYPost*i+YTopMargin,
                    width=100,
                    height=variableHeight)

                globals()[f"label_price{i}"] = Label(window, 
                    text=gameData[i-1]["price"],
                    fg = "#c7d5e0",
                    bg = "#313d4b",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_price{i}"].place(
                    x=950,
                    y=relativeYPost*i+YTopMargin,
                    width=65,
                    height=variableHeight)

                globals()[f"button_open_game{i}"] = Button(window, 
                    text="Info",
                    fg = "#c7d5e0",
                    bg = "#313d4b",
                    font = "Arial 12"
                    )
                globals()[f"button_open_game{i}"].place(x=1015,y=relativeYPost*i+YTopMargin,width=50,height=variableHeight)
            else:
                globals()[f"label_name{i}"] = Label(window, 
                    text=gameData[i-1]["name"],
                    fg = "#c7d5e0",
                    bg = "#1b2838",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_name{i}"].place(
                    x=200,
                    y=relativeYPost*i+YTopMargin,
                    width=450,
                    height=variableHeight)

                globals()[f"label_platform{i}"] = Label(window, 
                    text=gameData[i-1]["platforms"],
                    fg = "#c7d5e0",
                    bg = "#1b2838",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_platform{i}"].place(
                    x=650,
                    y=relativeYPost*i+YTopMargin,
                    width=200,
                    height=variableHeight)

                globals()[f"label_release{i}"] = Label(window, 
                    text=gameData[i-1]["release_date"],
                    fg = "#c7d5e0",
                    bg = "#1b2838",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_release{i}"].place(
                    x=850,
                    y=relativeYPost*i+YTopMargin,
                    width=100,
                    height=variableHeight)

                globals()[f"label_price{i}"] = Label(window, 
                    text=gameData[i-1]["price"],
                    fg = "#c7d5e0",
                    bg = "#1b2838",
                    font = "Arial 12",
                    anchor=W)
                globals()[f"label_price{i}"].place(
                    x=950,
                    y=relativeYPost*i+YTopMargin,
                    width=65,
                    height=variableHeight)

                globals()[f"button_open_game{i}"] = Button(window, 
                    text="Info",
                    fg = "#c7d5e0",
                    bg = "#1b2838",
                    font = "Arial 12"
                    )
                globals()[f"button_open_game{i}"].place(x=1015,y=relativeYPost*i+YTopMargin,width=50,height=variableHeight)



def destroy_games():
    for i in range(1,13): 
        globals()[f"label_name{i}"].destroy()
        globals()[f"label_platform{i}"].destroy()
        globals()[f"label_release{i}"].destroy()
        globals()[f"label_price{i}"].destroy()
        globals()[f"button_open_game{i}"].destroy()


def destroy_homescreen():
    # TI SnackBox controle knoppen
    UnlockSnackBoxButton.place_forget()
    LockSnackBoxButton.place_forget()

    # searchbox
    searchBox.place_forget()

    # searchbutton
    searchButton.place_forget()

    # filter
    # filter_selectie(options)

    # sort menu apply knop
    button_apply_sort.place_forget()

    #Filter apply knop
    button_apply_filter.place_forget()

    #Price options
    label_price_options.place_forget()

    # filter opties
    checkbutton_free_to_play.place_forget()
    checkbutton_early_access_option.place_forget()
    checkbutton_action_option.place_forget()
    checkbutton_adventure_option.place_forget()
    checkbutton_casual_option.place_forget()
    checkbutton_indie_option.place_forget()
    checkbutton_massively_multiplayer_option.place_forget()
    checkbutton_racing_option.place_forget()
    checkbutton_RPG_option.place_forget()
    checkbutton_simulation_option.place_forget()
    checkbutton_sports_option.place_forget()
    checkbutton_strategy_option.place_forget()

    #Price options
    label_filter_apply.place_forget()

    #prijs filter menu
    price_filter_menu.place_forget()
    
    #prijs filter menu
    filter_selection_menu.place_forget()

    #backwords button
    button_back.place_forget()

    #forward button
    button_forward.place_forget()

    # game list header
    label_name0.place_forget()

    label_platform0.place_forget()

    label_release0.place_forget()

    label_price0.place_forget()

    label_info0.place_forget()


# #most positive
# label_most_positive_ratings = Label(window, 
#     text="highest ratings:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_most_positive_ratings.place(
#     x=200,
#     y=relativeYPost*4+YTopMargin,
#     width=250,
#     height=variableHeight)

# data_most_positive_ratings = Label(window, 
#     text="**most_positive_ratings data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_most_positive_ratings.place(
#     x=450,
#     y=relativeYPost*4+YTopMargin,
#     width=350,
#     height=variableHeight)

# #ratio

# label_review_ratio = Label(window, 
#     text="best review ratio:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_review_ratio.place(
#     x=200,
#     y=relativeYPost*5+YTopMargin,
#     width=250,
#     height=variableHeight)


# data_review_ratio = Label(window, 
#     text="**review_ratio data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_review_ratio.place(
#     x=450,
#     y=relativeYPost*5+YTopMargin,
#     width=350,
#     height=variableHeight)

# 2e scherm AI statistiek


back_button = Button(window, 
text="<-- Back",
fg = "#c7d5e0",
bg = "#1b2838",
font = "Arial 12 bold",)

gamename_label = Label(window, 
    text="Game name: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

gamename_data = Label(window, 
    text="",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

gameplayer_number_label = Label(window, 
    text="Player count: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

gameplayer_number_data = Label(window, 
    text= "",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

game_info_label = Label(window, 
    text="Game description: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

game_info_data = Label(window, 
    text= "",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    wraplength=350
    )

achievements_label = Label(window, 
    text="achievements: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")

achievements_data = Label(window, 
    text= "achievements_placeholder",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    wraplength=350
    )
 #postive, negative en ration
#positive_ratings
positive_ratings_label = Label(window, 
    text="positive ratings: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")


positive_ratings_data = Label(window, 
    text= "positive_ratings",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    wraplength=350
    )

#negative_ratings

negative_ratings_label = Label(window, 
    text="negative ratings: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")


negative_ratings_data = Label(window, 
    text= "negative_ratings_placeholder",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    wraplength=350
    )

#review_ratio
review_ratio_label = Label(window, 
    text="review ratio: ",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")


review_ratio_data = Label(window, 
    text= "review_ratio_placeholder",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    wraplength=350
    )


def game_info_page(appid, game_name, achievements, positive_ratings, negative_ratings, review_ratio):

    back_button.place(x=20.0,
        y=120.0,
        width=110,
        height=25)

    gamename_label.place(
        x=150,
        y=20,
        width=150,
        height=variableHeight)

    gamename_data.config(text=game_name)
    gamename_data.place(
        x=300,
        y=20,
        width=350,
        height=variableHeight)



    #api helper + call
    api = apihelper.APIHelper()
    parameters = {
        f'appid': {appid}
    }
    # Vraag het aantal spelers voor een game op
    res = api.get_app_players(parameters)
    no_players = res['response']['player_count']



    gameplayer_number_label.place(
        x=150,
        y=55,
        width=150,
        height=variableHeight)

    gameplayer_number_data.config(text=no_players)

    gameplayer_number_data.place(
        x=300,
        y=55,
        width=350,
        height=variableHeight)



    #game info
    game_description = api.game_info_page(str(appid))[str(appid)]["data"]['short_description']
    # print(game_description)

    game_info_label.place(
        x=660,
        y=20,
        width=150,
        height=300)

    game_info_data.config(text=game_description)

    game_info_data.place(
        x=810,
        y=20,
        width=400,
        height=300)

    #achievements

    achievements_label.place(
        x=150,
        y=90,
        width=150,
        height=variableHeight)

    achievements_data.config(text=achievements)
    achievements_data.place(
        x=300,
        y=90,
        width=350,
        height=variableHeight)
    
    #place postive, negative en ratio
    positive_ratings_label.place(
    x=150,
    y=125,
    width=150,
    height=variableHeight)


    positive_ratings_data.config(text=positive_ratings)
    positive_ratings_data.place(
    x=300,
    y=125,
    width=350,
    height=variableHeight)

    #negative
    negative_ratings_label.place(
    x=150,
    y=160,
    width=150,
    height=variableHeight)

    negative_ratings_data.config(text=negative_ratings)
    negative_ratings_data.place(
    x=300,
    y=160,
    width=350,
    height=variableHeight)

    #ratio
    review_ratio_label.place(
    x=150,
    y=195,
    width=150,
    height=variableHeight)


    review_ratio_data.config(text=review_ratio)
    review_ratio_data.place(
    x=300,
    y=195,
    width=350,
    height=variableHeight)

def destroy_game_info_page():

    back_button.place_forget() 

    gamename_label.place_forget()

    gamename_data.place_forget() 

    gameplayer_number_label.place_forget() 

    gameplayer_number_data.place_forget() 

    game_info_label.place_forget() 

    game_info_data.place_forget() 

    achievements_label.place_forget() 

    achievements_data.place_forget() 

    positive_ratings_label.place_forget()

    positive_ratings_data.place_forget()

    negative_ratings_label.place_forget()

    negative_ratings_data.place_forget()

    review_ratio_label.place_forget()

    review_ratio_data.place_forget()

# game_info_page(440)
#window.mainloop()

