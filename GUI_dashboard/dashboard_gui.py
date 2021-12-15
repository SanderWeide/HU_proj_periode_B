from pathlib import Path
from tkinter import *
# ws = Tk()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title('Steam Dashboard')
window.geometry("1280x720")
window.configure(bg = "#2a475e")

# img = PhotoImage(relative_to_assets("steam_background.png"))
# label = Label(
#     ws,
#     image=img
# )
# label.place(x=0, y=0)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# def pop_up(timer, message):
#     pop_up = Toplevel(window)
#     pop_up.geometry("650x70")
#     pop_up.configure(bg = "#fcc63f")
#     pop_up.resizable(False, False)
#     Label(pop_up, 
#     text=message,
#     fg = "#212b5c",
#     bg = "#fcc63f",
#     font = "Arial 26 bold").pack(pady=10)
#     pop_up.after(timer, lambda: pop_up.destroy())


image_image_3 = PhotoImage(
    file=relative_to_assets("steam_resize.png"))
image_3 = canvas.create_image(
    60.0,
    60.0,
    image=image_image_3
)

# button_image_1 = PhotoImage(
#     file=relative_to_assets("button_1.png"))

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