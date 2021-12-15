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

appid = Label(window, 
    text="appid",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
appid.place(
    x=200,
    y=10.0,
    width=250,
    height=60)

name = Label(window, 
    text="name",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
name.place(
    x=200.0,
    y=70.0,
    width=250,
    height=60)

platforms = Label(window, 
    text="platforms",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
platforms.place(
    x=200,
    y=130.0,
    width=250,
    height=60)

required_age = Label(window, 
    text="required_age",
    fg = "#c7d5e0",
    bg = "#1b2838",
    font = "Arial 20 bold",
    anchor=E)
required_age.place(
    x=200.0,
    y=180.0,
    width=250,
    height=60)

# input_name = Text(
#     fg = "#212b5c",
#     bg = "white",
#     font = "Arial 36",
#     insertbackground="#212b5c")
# input_name.place(
#     x=530.0,
#     y=70.0,
#     width=700.0,
#     height=58.0
# )

# input_message = Text(
#     fg = "#212b5c",
#     bg = "white",
#     font = "Arial 24",
#     wrap='word',
#     insertbackground="#212b5c"
# )
# input_message.place(
#     x=530.0,
#     y=180.0,
#     width=600.0,
#     height=490.0
# )
window.mainloop()