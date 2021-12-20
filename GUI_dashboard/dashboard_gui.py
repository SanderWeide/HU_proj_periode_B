from pathlib import Path
from tkinter import *


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
    600.0,
    400.0,
    image=img
)


steamlogo = PhotoImage(
    file=relative_to_assets("steam_resize.png"))
steam_logo = canvas.create_image(
    60.0,
    60.0,
    image=steamlogo
)

label_appid = Label(window, 
    text="app id:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
label_appid.place(
    x=200,
    y=10.0,
    width=250,
    height=60)

data_appid = Label(window, 
    text="**app id data field**",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold")
data_appid.place(
    x=450,
    y=10.0,
    width=350,
    height=60)

label_name = Label(window, 
    text="name:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
label_name.place(
    x=200.0,
    y=70.0,
    width=250,
    height=60)

data_name = Label(window, 
    text="**name data field**",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold")
data_name.place(
    x=450.0,
    y=70.0,
    width=350,
    height=60)

label_platforms = Label(window, 
    text="platforms:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
label_platforms.place(
    x=200,
    y=130.0,
    width=250,
    height=60)

data_platforms = Label(window, 
    text="**platforms data field**",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold")
data_platforms.place(
    x=450,
    y=130.0,
    width=350,
    height=60)

label_required_age = Label(window, 
    text="required age:",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
label_required_age.place(
    x=200.0,
    y=180.0,
    width=250,
    height=60)

data_required_age = Label(window, 
    text="**required age data field**",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold")
data_required_age.place(
    x=450.0,
    y=180.0,
    width=350,
    height=60)


# window.mainloop()