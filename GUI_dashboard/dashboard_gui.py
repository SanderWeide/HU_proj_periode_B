from pathlib import Path
from tkinter import *

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

# searchbox
searchBox = Text(window,
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12")
searchBox.place(
    x=200,
    y=25,
    width=540,
    height=25)

searchButton = Button (window, text="Zoeken")

searchButton.place(
    x=740,
    y=25,
    width=60,
    height=25)

# selectie menu sorteer opties
def filter_selectie(options):
    global value_option_menu

    value_option_menu = StringVar(window)
    value_option_menu.set(options[0]) # default value
    
    filter_selection_menu = OptionMenu(window, value_option_menu, *options,)
    filter_selection_menu.place(
        x=850.0,
        y=25.0,
        width=160,
        height=25
    )

options = [
    'Sort By',
    'Date  (new - old)',
    'Date  (old - new)',
    'Price (ascending)',
    'Price (descending)']

filter_selectie(options)

# sort menu apply knop
button_apply_sort = Button(window, 
    text="Sort",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold"
    )
button_apply_sort.place(x=1015,y=25.0,width=50,height=25)


#Filter apply knop
button_apply_filter = Button(window, 
    text="Apply Filter",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)
button_apply_filter.place(x=20.0,y=120.0,width=160,height=25)


#Price options
label_price_options = Label(window, 
    text="Game category",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)
label_price_options.place(x=20.0,y=155.0,width=160,height=25)

# filter opties
Free_to_Play_option = IntVar()
Checkbutton(window, text="Free to Play", variable=Free_to_Play_option).place(x=20.0,y=180.0,width=160,height=25)
Early_Access_option = IntVar()
Checkbutton(window, text="Early Access", variable=Early_Access_option).place(x=20.0,y=200.0,width=160,height=25)
Action_option = IntVar()
Checkbutton(window, text="Action", variable=Action_option).place(x=20.0,y=220.0,width=160,height=25)
Adventure_option = IntVar()
Checkbutton(window, text="Adventure", variable=Adventure_option).place(x=20.0,y=240.0,width=160,height=25)
Casual_option = IntVar()
Checkbutton(window, text="Casual", variable=Casual_option).place(x=20.0,y=260.0,width=160,height=25)
Indie_option = IntVar()
Checkbutton(window, text="Indie", variable=Indie_option).place(x=20.0,y=280.0,width=160,height=25)
Massively_Multiplayer_option = IntVar()
Checkbutton(window, text="Massively Multiplayer", variable=Massively_Multiplayer_option).place(x=20.0,y=300.0,width=160,height=25)
Racing_option = IntVar()
Checkbutton(window, text="Racing", variable=Racing_option).place(x=20.0,y=320.0,width=160,height=25)
RPG_option = IntVar()
Checkbutton(window, text="RPG", variable=RPG_option).place(x=20.0,y=340.0,width=160,height=25)
Simulation_option = IntVar()
Checkbutton(window, text="Simulation", variable=Simulation_option).place(x=20.0,y=360.0,width=160,height=25)
Sports_option = IntVar()
Checkbutton(window, text="Sports", variable=Sports_option).place(x=20.0,y=380.0,width=160,height=25)
Strategy_option = IntVar()
Checkbutton(window, text="Strategy", variable=Strategy_option).place(x=20.0,y=400.0,width=160,height=25)

#Price options
label_filter_apply = Label(window, 
    text="Price category",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold",
    anchor=E)
label_filter_apply.place(x=20.0,y=435.0,width=160,height=25)

#prijs filter menu
def price_filter_menu(price_options):
    global value_price_menu

    value_price_menu = StringVar(window)
    value_price_menu.set(price_options[0]) # default value
    
    filter_selection_menu = OptionMenu(window, value_price_menu, *price_options,)
    filter_selection_menu.place(
        x=20.0,
        y=460.0,
        width=160,
        height=25
    )

price_options = [
    'Select price range',
    'Games under €5',
    'Games under €10',
    'Games under €20',
    'Games under €40',
    'Games over €40']

price_filter_menu(price_options)

#backwords button
button_back = Button(window, 
    text="<-- Back",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")
button_back.place(x=300.0,y=650.0,width=160,height=25)


#forward button
button_forward = Button(window, 
    text="Next -->",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12 bold")
button_forward.place(x=800.0,y=650.0,width=160,height=25)












label_name0 = Label(window, 
    text="Name:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)
label_name0.place(
    x=200,
    y=relativeYPost*0+YTopMargin,
    width=450,
    height=variableHeight)

label_platform0 = Label(window, 
    text="Platform:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)
label_platform0.place(
    x=650,
    y=relativeYPost*0+YTopMargin,
    width=200,
    height=variableHeight)

label_release0 = Label(window, 
    text="Date:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)
label_release0.place(
    x=850,
    y=relativeYPost*0+YTopMargin,
    width=100,
    height=variableHeight)

label_price0 = Label(window, 
    text="Price:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)
label_price0.place(
    x=950,
    y=relativeYPost*0+YTopMargin,
    width=65,
    height=variableHeight)

label_info0 = Label(window, 
    text="Info:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 12",
    anchor=W)
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


# window.mainloop()