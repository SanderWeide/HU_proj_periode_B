from pathlib import Path
from tkinter import *
import json

variableHeight = 50
relativeYPost = 50
YTopMargin = 65

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
    'Date  (new - old)',
    'Date  (old - new)',
    'Price (ascending)',
    'Price (descending)']

filter_selectie(options)

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

# filter genres
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

#Prijs filters
# Games_under_5_option = IntVar()
# Checkbutton(window, text="Games under €5 ", variable=Games_under_5_option).place(x=20.0,y=460.0,width=160,height=25)
# Games_under_10_option = IntVar()
# Checkbutton(window, text="Games under €10 ", variable=Games_under_10_option).place(x=20.0,y=480.0,width=160,height=25)
# Games_under_20_option = IntVar()
# Checkbutton(window, text="Games under €20", variable=Games_under_20_option).place(x=20.0,y=500.0,width=160,height=25)
# Games_over_40_option = IntVar()
# Checkbutton(window, text="Games over €40", variable=Games_over_40_option).place(x=20.0,y=520.0,width=160,height=25)

# #data veld
# json_filename = 'test.json'

# with open(json_filename, 'r') as inside:
#     data = json.load(inside)

# data_field = Text(window, state='normal', height=35, width=120)
# data_field.place(x=200, y=100)
# data_field.insert('1.0', str(data))


# appid
# label_appid = Label(window, 
#     text="app id:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_appid.place(
#     x=200,
#     y=relativeYPost*0+YTopMargin,
#     width=250,
#     height=variableHeight)

for i in range(0,5):
    data_appid = Label(window, 
        text="**app id data field**",
        fg = "#c7d5e0",
        bg = "#1b2838",
        font = "Arial 12 bold")
    data_appid.place(
        x=450,
        y=relativeYPost*(0+i)+YTopMargin,
        width=350,
        height=variableHeight)

# name
for i in range(0,5):
    label_name = Label(window, 
        text="name:",
        fg = "#c7d5e0",
        bg = "#1b2838",
        font = "Arial 12 bold",
        anchor=E)
    label_name.place(
        x=200,
        y=relativeYPost*(1+i)+YTopMargin,
        width=250,
        height=variableHeight)

# data_name = Label(window, 
#     text="**name data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_name.place(
#     x=450,
#     y=relativeYPost*1+YTopMargin,
#     width=350,
#     height=variableHeight)

# # platforms
# label_platforms = Label(window, 
#     text="platforms:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_platforms.place(
#     x=200,
#     y=relativeYPost*2+YTopMargin,
#     width=250,
#     height=variableHeight)

# data_platforms = Label(window, 
#     text="**platforms data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_platforms.place(
#     x=450,
#     y=relativeYPost*2+YTopMargin,
#     width=350,
#     height=variableHeight)

# # required age
# label_required_age = Label(window, 
#     text="required age:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_required_age.place(
#     x=200,
#     y=relativeYPost*3+YTopMargin,
#     width=250,
#     height=variableHeight)

# data_required_age = Label(window, 
#     text="**required age data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_required_age.place(
#     x=450,
#     y=relativeYPost*3+YTopMargin,
#     width=350,
#     height=variableHeight)

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


#window.mainloop()