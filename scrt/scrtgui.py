from tkinter import Toplevel, Label, PhotoImage


def secretphoto():
    memewindow = Toplevel()
    memewindow.title("Secret Meme")
    secret = PhotoImage(file='assets/images/download.png')
    label = Label(memewindow, image=secret)
    label.image = secret
    label.pack()

    