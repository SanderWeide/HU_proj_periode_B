from pathlib import Path
from tkinter import *
from tkinter import ttk

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

def selectiemenu_setup():
    mylabel = Label(window, text=selectiemenu.get()).pack

options = [
    'Datum (nieuw - oud)',
    'Datum (oud - nieuw)',
    'Prijs (oplopend)',
    'Prijs (aflopend)']

selectiemenu = ttk.Combobox(window, value= options)
selectiemenu.current(0)
selectiemenu.bind("<<Selectiemenukeuze>>", selectiemenu_setup)
selectiemenu.place(
        x=850.0,
        y=25.0,
        width=160,
        height=25 )


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

# data_appid = Label(window, 
#     text="**app id data field**",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold")
# data_appid.place(
#     x=450,
#     y=relativeYPost*0+YTopMargin,
#     width=350,
#     height=variableHeight)

# # name
# label_name = Label(window, 
#     text="name:",
#     fg = "#c7d5e0",
#     bg = "#1b2838",
#     font = "Arial 12 bold",
#     anchor=E)
# label_name.place(
#     x=200,
#     y=relativeYPost*1+YTopMargin,
#     width=250,
#     height=variableHeight)

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


window.mainloop()