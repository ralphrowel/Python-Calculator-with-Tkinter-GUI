from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Ralph Calculator")
window.config(background="#424b59")

icon = PhotoImage(file="gui/images/calculatoricon.png")
window.iconphoto(True, icon)

title = Label(window, text="Created by Ralphrowel!", 
              font=('Arial', 10, 'bold'),
              fg='white',
              bg="#424b59",
              relief=RAISED,
              bd=2,
              padx=2
              )

title.pack()
# title.place(x=0,y=0)

window.mainloop()