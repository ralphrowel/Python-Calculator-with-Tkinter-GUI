from tkinter import *
from scrt.scrtgui import secretphoto
from logic.solve import calculate

def start_app():
    window = Tk()
    # window.geometry("420x420")
    window.title("Ralph Calculator")
    window.config(background="#424b59")

    icon = PhotoImage(file="assets/images/calculatoricon.png")
    window.iconphoto(True, icon)

    outputint = " "

    def buttonclicked(char):
        current = outputlabel['text']
        if current == "" and char in "+-x÷":
            return
        outputlabel.config(text=current + str(char))

    def buttontotalclicked():
        expr = outputlabel['text'].replace('x','*').replace('÷','/')
        if expr.strip() == "20":
            secretphoto()
        else:
            result = calculate(expr)
            outputlabel.config(text=result)

    def buttondeleteclicked():
        outputlabel.config(text=outputint)

    title = Label(window, text="Created by Ralphrowel!", 
                  font=('Arial', 10, 'bold'),
                  fg='white',
                  bg="#424b59",
                  relief=RAISED,
                  bd=2,
                  padx=2
                  )

    outputlabel = Label(window, 
                   text=outputint,
                   font=('Digital-7', 15),
                   fg="#699435",
                   bg="#98d060",
                   relief=SOLID,
                   bd=2,
                   padx=5, pady=5,
                   width=20, height=2
                   )

    buttonframe = Frame(window, bg="#424b59")

    buttons = [
        ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('÷', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('x', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
        ('0', 3, 0), ('c', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ]

    for text, r, c in buttons:
        if text == '=':
            cmd = buttontotalclicked
            bgc = "#3d89f6"
        elif text == 'c':
            cmd = buttondeleteclicked
            bgc = "#e85958"
        elif text in '+-x÷':
            cmd = lambda t=text: buttonclicked(t)
            bgc = "#e85958"
        else:
            cmd = lambda t=text: buttonclicked(t)
            bgc = "#828f9f"

        Button(buttonframe, text=text, command=cmd,
               font=('Digital-7', 15, 'bold'),
               fg="#fffffe",
               bg=bgc,
               activebackground="#fffffe",
               activeforeground="#828f9f",
               height=1, width=2,
               padx=9, pady=9
               ).grid(row=r, column=c, padx=5, pady=5)

    title.pack()
    outputlabel.pack(padx=5, pady=5)
    buttonframe.pack(pady=5)

    window.mainloop()
