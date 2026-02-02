from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Ralph Calculator")
window.config(background="#424b59")

icon = PhotoImage(file="gui/images/calculatoricon.png")
window.iconphoto(True, icon)


outputint = " "


def buttonclicked(char):
    current = outputlabel['text']
    outputlabel.config(text=current + str(char))

def buttontotalclicked():
    expr = outputlabel['text'].replace('x','*').replace('÷','/')
    result = calculate(expr)
    outputlabel.config(text=result)

def buttondeleteclicked():
    outputlabel.config(text=outputint)

def calculate(expression):
    try:
        return eval(expression)
    except Exception:
        return "Error"


nameme = Label(window, text="Created by Ralphrowel!", 
              font=('Arial', 10, 'bold'),
              fg='white',
              bg="#424b59",
              relief=RAISED,
              bd=2,
              )

outputlabel = Label(window, 
               text=outputint,
               font=('Digital-7', 15),
               fg="#699435",
               bg="#98d060",
               relief=SOLID,
               bd=2,
               padx= 5, pady= 5,
               width=20, height=2
               )

buttonframe = Frame(window, bg="#424b59")


button1 = Button(buttonframe,text='1',
                 command=lambda: buttonclicked('1'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button2 = Button(buttonframe,text='2',
                 command=lambda: buttonclicked('2'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button3 = Button(buttonframe,text='3',
                 command=lambda: buttonclicked('3'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button4 = Button(buttonframe,text='4',
                 command=lambda: buttonclicked('4'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button5 = Button(buttonframe,text='5',
                 command=lambda: buttonclicked('5'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button6 = Button(buttonframe,text='6',
                 command=lambda: buttonclicked('6'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button7 = Button(buttonframe,text='7',
                 command=lambda: buttonclicked('7'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button8 = Button(buttonframe,text='8',
                 command=lambda: buttonclicked('8'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button9 = Button(buttonframe,text='9',
                 command=lambda: buttonclicked('9'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )
button0 = Button(buttonframe,text='0',
                 command=lambda: buttonclicked('0'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#828f9f",
                 activebackground="#fffffe",
                 activeforeground="#828f9f",
                 height=1, width=2,
                 padx=9, pady=9
                 )

buttondivide = Button(buttonframe,text='÷',
                 command=lambda: buttonclicked('÷'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#e85958",
                 height=1, width=2,
                 padx=9, pady=9
                 )
buttonmultiply = Button(buttonframe,text='x',
                 command=lambda: buttonclicked('x'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#e85958",
                 height=1, width=2,
                 padx=9, pady=9
                 )
buttonminus = Button(buttonframe,text='-',
                 command=lambda: buttonclicked('-'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#e85958",
                 height=1, width=2,
                 padx=9, pady=9
                 )
buttonsum = Button(buttonframe,text='+',
                 command=lambda: buttonclicked('+'),
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#e85958",
                 height=1, width=2,
                 padx=9, pady=9
                 )
buttondelete = Button(buttonframe,text='c',
                 command=buttondeleteclicked,
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#e85958",
                 height=1, width=2,
                 padx=9, pady=9
                 )
buttontotal = Button(buttonframe,text='=',
                 command=buttontotalclicked,
                 font=('Digital-7', 15, 'bold'),
                 fg="#fffffe",
                 bg="#3d89f6",
                 height=1, width=2,
                 padx=9, pady=9
                 )


nameme.pack()
outputlabel.pack(padx=5, pady=5)
buttonframe.pack(pady=5)
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=0, column=2, padx=5, pady=5)
buttondivide.grid(row=0, column=3, padx=5, pady=5)

button4.grid(row=1, column=0, padx=5, pady=5,)
button5.grid(row=1, column=1, padx=5, pady=5,)
button6.grid(row=1, column=2, padx=5, pady=5,)
buttonmultiply.grid(row=1, column=3, padx=5, pady=5,)

button7.grid(row=2, column=0, padx=5, pady=5,)
button8.grid(row=2, column=1, padx=5, pady=5,)
button9.grid(row=2, column=2, padx=5, pady=5,)
buttonminus.grid(row=2, column=3, padx=5, pady=5,)

button0.grid(row=3, column=0, padx=5, pady=5,)
buttondelete.grid(row=3, column=1, padx=5, pady=5,)
buttontotal.grid(row=3, column=2, padx=5, pady=5,)
buttonsum.grid(row=3, column=3, padx=5, pady=5,)



window.mainloop()