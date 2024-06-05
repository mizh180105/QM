from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\tkinterds\build1\assets\frame0")
class RegistrationForm:
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)
    def open_gui_and_close_window(self):
        self.window.destroy()
        subprocess.run(["python", "D:\tkinterds\\btap\\gui.py"])
    def __init__(self):
        self.window = Tk()
        self.window.geometry("750x500")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Đăng ký")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=750,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            750.0,
            500.0,
            fill="#FFFFFF",
            outline=""
        )

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            136.0,
            250.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            447.0,
            250.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            310.0,
            46.0,
            anchor="nw",
            text="Đăng ký",
            fill="#0093FF",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            310.0,
            82.0,
            anchor="nw",
            text="Bắt đầu với trải nghiệm",
            fill="#A1A1A1",
            font=("Inter Light", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            511.5,
            161.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F3F3F3",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=315.0,
            y=135.0,
            width=393.0,
            height=51.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            511.5,
            244.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F3F3F3",
            fg="#000716",
            highlightthickness=0,
            show="•"  # Show a dot as the hidden character
        )
        self.entry_2.place(
            x=315.0,
            y=218.0,
            width=393.0,
            height=51.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            511.5,
            327.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F3F3F3",
            fg="#000716",
            highlightthickness=0,
            show="•"  
        )
        self.entry_3.place(
            x=315.0,
            y=301.0,
            width=393.0,
            height=51.0
        )

        self.canvas.create_text(
            310.0,
            117.0,
            anchor="nw",
            text="Email/ Số điện thoại",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            310.0,
            200.0,
            anchor="nw",
            text="Mật khẩu",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            310.0,
            283.0,
            anchor="nw",
            text="Xác nhận mật khẩu",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_gui_and_close_window,
            relief="flat"
        )
        self.button_1.place(
            x=437.0,
            y=394.0,
            width=150.0,
            height=50.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()
registration_form = RegistrationForm()