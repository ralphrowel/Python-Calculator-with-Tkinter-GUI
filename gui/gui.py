import tkinter as tk
from tkinter import PhotoImage
from logic.solve import calculate
from scrt.scrtgui import secretphoto

def start_app():

    window = tk.Tk()
    window.title("Ralph Calculator")
    window.config(background="#424b59")

    icon = PhotoImage(file="assets/images/calculatoricon.png")
    window.iconphoto(True, icon)

    output_value = ""

    def buttonclicked(char):
        nonlocal output_value

        if output_value == "" and char in "+-x÷":
            return

        output_value += char
        outputlabel.config(text=output_value)

    def buttontotalclicked():
        nonlocal output_value

        expr = output_value.replace('x', '*').replace('÷', '/')

        if expr.strip() == "20":
            secretphoto()
            return

        result = calculate(expr)
        output_value = str(result)
        outputlabel.config(text=output_value)

    def buttondeleteclicked():
        nonlocal output_value
        output_value = ""
        outputlabel.config(text="")

    outputlabel = tk.Label(
        window,
        text="",
        font=('Arial', 18),
        width=20,
        height=2
    )
    outputlabel.pack(pady=10)

    buttonframe = tk.Frame(window)
    buttonframe.pack()

    buttons = [
        ('1',0,0), ('2',0,1), ('3',0,2), ('÷',0,3),
        ('4',1,0), ('5',1,1), ('6',1,2), ('x',1,3),
        ('7',2,0), ('8',2,1), ('9',2,2), ('-',2,3),
        ('0',3,0), ('c',3,1), ('=',3,2), ('+',3,3),
    ]

    for (text,row,col) in buttons:
        if text == '=':
            cmd = buttontotalclicked
        elif text == 'c':
            cmd = buttondeleteclicked
        else:
            cmd = lambda t=text: buttonclicked(t)

        tk.Button(
            buttonframe,
            text=text,
            width=4,
            height=2,
            command=cmd
        ).grid(row=row, column=col, padx=5, pady=5)

    window.mainloop()
