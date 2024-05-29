from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\tkinterds\build0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.geometry("750x500")
window.configure(bg = "#DCDCDC")
window.title("Ứng dụng trộn đề")
class dangnhap():
    canvas = Canvas(
        window,
        bg="#DCDCDC",
        height=500,
        width=750,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        750.0,
        500.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        305.0,
        40.0,
        anchor="nw",
        text="Welcome back!",
        fill="#0089EC",
        font=("SegoeUI Bold", 30 * -1)
    )

    canvas.create_text(
        305.0,
        80.0,
        anchor="nw",
        text="Đăng nhập để tiếp tục",
        fill="#8B8B8B",
        font=("SegoeUI Bold", 15 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        509.0,
        164.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        relief="solid",
        font=("SegoeUI Semilight", 15 * -1),
        highlightcolor="#A9A9A9",
        highlightbackground="#A9A9A9",
        highlightthickness=1
    )
    entry_1.place(
        x=308.0,
        y=140.0,
        width=402.0,
        height=46.0
    )

    canvas.create_text(
        308.0,
        120.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("SegoeUI Semilight", 15 * -1)
    )

    canvas.create_text(
        308.0,
        198.0,
        anchor="nw",
        text="Mật khẩu",
        fill="#000000",
        font=("SegoeUI Semilight", 15 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        509.0,
        243.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show="•",
        relief="solid",
        highlightcolor="#A9A9A9",
        highlightbackground="#A9A9A9",
        font=("SegoeUI Semilight", 15 * -1)
    )
    entry_2.configure(highlightbackground="#A9A9A9", highlightcolor="#A9A9A9", highlightthickness=1)
    entry_2.place(
        x=308.0,
        y=219.0,
        width=402.0,
        height=46.0
    )

    canvas.create_rectangle(
        307.0,
        376.99999999999994,
        468.0,
        378.0,
        fill="#757575",
        outline="")

    canvas.create_rectangle(
        535.0,
        377.0,
        710.0,
        378.0,
        fill="#757575",
        outline="")

    canvas.create_text(
        485.0,
        358.0,
        anchor="nw",
        text="Hoặc",
        fill="#7D7D7D",
        font=("SegoeUI Semibold", 15 * -1)
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
    )
    button_1.place(
        x=402.0,
        y=301.0,
        width=200.0,
        height=48.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=402.0,
        y=396.0,
        width=200.0,
        height=48.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        140.0,
        250.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
