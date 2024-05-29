from pathlib import Path
from tkinter import T, Canvas, Text, Button, PhotoImage, font, filedialog, messagebox
import tkinter as tk
from docx import Document
import random
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\tkinterds\build\assets\frame0")
textbox = Text(
                    bd=0,
                    bg="#FFFFFF",
                    fg="#000716",
                    highlightthickness=0
                )
textbox.place(
                    x=91.0,
                    y=156.0,
                    width=1119.0,
                    height=642.0
                )
class QM:
    
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    def make_text_bold(textbox):
        current_font = font.Font(font=textbox['font'])
        current_font.configure(weight='bold')
        textbox.configure(font=current_font)
    def make_text_italic():
        current_font = font.Font(font=textbox['font'])
        current_font.configure(slant='italic')
        textbox.configure(font=current_font)
    def make_text_underline():
        current_font = font.Font(font=textbox['font'])
        current_font.configure(underline=True)
        textbox.configure(font=current_font)
    def make_text_subscript():
        current_font = font.Font(font=textbox['font'])
        current_font.configure(size=8)
        textbox.configure(font=current_font, spacing3=5)
    def make_text_superscript():
        current_font = font.Font(font=textbox['font'])
        current_font.configure(size=8)
        textbox.configure(font=current_font, spacing1=-5)
    def align_text_left():
        textbox.tag_configure("left", justify='left')
        textbox.tag_add("left", 1.0, "end")
    def align_text_center():
        textbox.tag_configure("center", justify='center')
        textbox.tag_add("center", 1.0, "end")
    def align_text_right():
        textbox.tag_configure("right", justify='right')
        textbox.tag_add("right", 1.0, "end")
    def justify_text():
        textbox.tag_configure("justify", justify='both')
        textbox.tag_add("justify", 1.0, "end")
    def insert_pi():
        textbox.insert("end", "π")
    def insert_infinity():
        textbox.insert("end", "∞")
    def insert_sigma():
        textbox.insert("end", "Σ")
    def insert_integral():
        textbox.insert("end", "∫")
    def insert_sqrt():
        textbox.insert("end", "√")
    def insert_approx():
        textbox.insert("end", "≈")
    def insert_alpha():
        textbox.insert("end", "α")
    def insert_beta():
        textbox.insert("end", "β")
    def insert_delta():
        textbox.insert("end", "δ")
    def insert_leq():
        textbox.insert("end", "≤")
    def insert_geq():
        textbox.insert("end", "≥")
    def insert_neq():
        textbox.insert("end", "≠")
    def adjust_font_size(size):
        textbox['font'] = font.Font(size=int(size))
    def adjust_font(font_name):
        textbox['font'] = font.Font(family=font_name)
    def open_word_file():
        file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
        if file_path:
            doc = Document(file_path)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            textbox.insert('1.0', '\n'.join(full_text))
    def mix_questions_and_answers():
        content = textbox.get('1.0', 'end').strip().split('\n')
        questions = [line for line in content if line.startswith('Q:')]
        answers = [line for line in content if line.startswith('A:')]
        if len(questions) != len(answers):
            messagebox.showerror("Error")
            return
        qa_pairs = list(zip(questions, answers))
        random.shuffle(qa_pairs)
        shuffled_questions, shuffled_answers = zip(*qa_pairs)
        textbox.delete('1.0', 'end')
        for i in range(len(shuffled_questions)):
            textbox.insert('end', shuffled_questions[i] + '\n')
            textbox.insert('end', shuffled_answers[i] + '\n')

    def export_to_word():
        content = textbox.get('1.0', 'end').strip().split('\n')
        doc = Document()
        for line in content:
            doc.add_paragraph(line)
        doc.save('output.docx')
    window = tk.Tk()
    window.title("Question mixing")
    window.geometry("1300x800")
    window.configure(bg = "#D1D1D1")
    font_size = tk.StringVar()
    canvas = Canvas(
                    window,
                    bg="#D1D1D1",
                    height=800,
                    width=1300,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge"
                )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
                    0.0,
                    0.0,
                    1300.0,
                    800.0,
                    fill="#E5E5E5",
                    outline="")

    canvas.create_rectangle(
                    0.0,
                    0.0,
                    1300.0,
                    110.0,
                    fill="#D3D3D3",
                    outline="")

    canvas.create_rectangle(
                    421.0,
                    58.0,
                    423.0,
                    90.0,
                    fill="#979797",
                    outline="")

    canvas.create_rectangle(
                    604.0,
                    58.0,
                    606.0,
                    90.0,
                    fill="#979797",
                    outline="")

    canvas.create_rectangle(
                    774.0,
                    58.0,
                    776.0,
                    90.0,
                    fill="#979797",
                    outline="")

    canvas.create_text(
                    191.0,
                    94.0,
                    anchor="nw",
                    text="Phông chữ",
                    fill="#000000",
                    font=("SegoeUI Semilight", 12 * -1)
                )

    canvas.create_text(
                    488.0,
                    94.0,
                    anchor="nw",
                    text="Căn chỉnh",
                    fill="#000000",
                    font=("SegoeUI Semilight", 12 * -1)
                )

    canvas.create_text(
                    651.0,
                    94.0,
                    anchor="nw",
                    text="Ký tự đặc biệt",
                    fill="#000000",
                    font=("SegoeUI Semilight", 12 * -1)
                )

    font_name = tk.StringVar()  
    menu_button = tk.Menubutton(window, text="                 >", relief="raised")
    menu_button.place(x=20.0, y=65.0, width=80.0, height=20.0)
    menu = tk.Menu(menu_button, tearoff=False)
    menu_button["menu"] = menu
    fonts = ['Helvetica', 'Times', 'Arial']  # Add more fonts as needed
    for f in fonts:
        menu.add_radiobutton(label=f, variable=font_name, command=lambda f=f: adjust_font(f))
    entry = tk.Entry(window, textvariable=font_name)
    entry.place(x=20.0, y=65.0, width=60.0, height=20.0)

    menu_button = tk.Menubutton(window, text="     >", relief="raised")
    menu_button.place(x=190.0, y=65.0, width=40.0, height=20.0)
    menu = tk.Menu(menu_button, tearoff=False)
    menu_button["menu"] = menu
    for size in range(10, 31, 2):  
        menu.add_radiobutton(label=str(size), variable=font_size, command=lambda size=size: adjust_font_size(size))
    entry = tk.Entry(window, textvariable=font_size)
    entry.place(x=190.0, y=65.0, width=20.0, height=20.0)

    canvas.create_rectangle(
                    0.0,
                    1.0,
                    1300.0,
                    51.0,
                    fill="#D9D9D9",
                    outline="")
    button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
    button_1 = Button(
            window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= make_text_bold(textbox),
            relief="flat"
                )
    button_1.place(
            x=247.0,
            y=65.0,
            width=20.0,
            height=20.0
                )
    button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
    button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=make_text_italic,
            relief="flat"
            )
    button_2.place(
            x=282.0,
            y=65.0,
            width=20.0,
            height=20.0
            )

    button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
    button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=make_text_underline,
            relief="flat"
                )
    button_3.place(
            x=317.0,
            y=65.0,
            width=20.0,
            height=20.0
                )
    button_image_4 = PhotoImage(
                file=relative_to_assets("button_4.png"))
    button_4 = Button(
                    image=button_image_4,
                    borderwidth=0,
                    highlightthickness=0,
                    command=open_word_file,
                    relief="flat"
                )
    button_4.place(
                    x=20.0,
                    y=17.0,
                    width=88.0,
                    height=19.0
                )

    button_image_5 = PhotoImage(
                file=relative_to_assets("button_5.png"))
    button_5 = Button(
                    image=button_image_5,
                    borderwidth=0,
                    highlightthickness=0,
                    command=mix_questions_and_answers,
                    relief="flat"
                )
    button_5.place(
                    x=131.0,
                    y=17.0,
                    width=88.0,
                    height=19.0
                )

    button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
    button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=export_to_word,
            relief="flat"
                )
    button_6.place(
            x=242.0,
            y=17.0,
            width=88.0,
            height=19.0
                )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=make_text_subscript,
            relief="flat"
                )
    button_7.place(
            x=349.0,
            y=67.0,
            width=21.0,
            height=20.0
                )

    button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
    button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=make_text_superscript,
            relief="flat"
                )
    button_8.place(
            x=381.0,
            y=65.0,
            width=21.0,
            height=20.0
                )

    button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
    button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=align_text_left,
            relief="flat"
                )
    button_9.place(
            x=438.0,
            y=65.0,
            width=21.0,
            height=20.0
                )

    button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
    button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=align_text_center,
            relief="flat"
                )
    button_10.place(
            x=479.0,
            y=64.0,
            width=21.0,
            height=20.0
                )

    button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
    button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command= align_text_right(),
            relief="flat"
                )
    button_11.place(
            x=520.0,
            y=65.0,
            width=21.0,
            height=20.0
                )

    button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
    button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=justify_text,
                    relief="flat"
                )
    button_12.place(
            x=561.0,
            y=65.0,
            width=21.0,
            height=20.0
                )

    button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
    button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=insert_pi,
            relief="flat"
                )
    button_13.place(
            x=614.0,
            y=52.0,
            width=19.0,
            height=20.0
                )

    button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
    button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=insert_infinity,
            relief="flat"
                )
    button_14.place(
            x=640.0,
            y=52.0,
            width=19.0,
            height=17.0
                )

    button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
    button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=insert_sigma,
            relief="flat"
                )
    button_15.place(
            x=666.0,
            y=52.0,
            width=19.0,
            height=19.0
                )

    button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
    button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=insert_sqrt,
            relief="flat"
                )
    button_16.place(
            x=713.0,
            y=53.0,
            width=19.0,
            height=18.0
                )

    button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
    button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=insert_approx,
            relief="flat"
                )
    button_17.place(
            x=738.0,
            y=52.0,
            width=19.0,
            height=19.0
                )

    button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
    button_18 = Button(
            image=button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=insert_integral,
            relief="flat"
                )
    button_18.place(
            x=690.0,
            y=53.0,
            width=19.0,
            height=18.0
                )

    button_image_19 = PhotoImage(
            file=relative_to_assets("button_19.png"))
    button_19 = Button(
            image=button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=insert_alpha,
            relief="flat"
                )
    button_19.place(
            x=614.0,
            y=71.0,
            width=19.0,
            height=19.0
                )

    button_image_20 = PhotoImage(
            file=relative_to_assets("button_20.png"))
    button_20 = Button(
            image=button_image_20,
            borderwidth=0,
            highlightthickness=0,
            command=insert_beta,
            relief="flat"
                )
    button_20.place(
            x=640.0,
            y=71.0,
            width=19.0,
            height=19.0
                )

    button_image_21 = PhotoImage(
            file=relative_to_assets("button_21.png"))
    button_21 = Button(
            image=button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=insert_delta,
            relief="flat"
                )
    button_21.place(
            x=666.0,
            y=71.0,
            width=19.0,
            height=18.0
                )

    button_image_22 = PhotoImage(
            file=relative_to_assets("button_22.png"))
    button_22 = Button(
            image=button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=insert_leq,
            relief="flat"
                )
    button_22.place(
            x=689.0,
            y=71.0,
            width=19.0,
            height=18.0
                )

    button_image_23 = PhotoImage(
            file=relative_to_assets("button_23.png"))
    button_23 = Button(
            image=button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command= insert_geq(),
            relief="flat"
                )
    button_23.place(
            x=714.0,
            y=71.0,
            width=19.0,
            height=18.0
                )

    button_image_24 = PhotoImage(
            file=relative_to_assets("button_24.png"))
    button_24 = Button(
            image=button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=insert_neq,
            relief="flat"
                )
    button_24.place(
            x=738.0,
            y=71.0,
                    width=19.0,
                    height=19.0
                )

    window.resizable(False, False)
    window.mainloop()  
