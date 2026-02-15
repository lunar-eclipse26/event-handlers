from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x300")
def msg():
    messagebox.showwarning("ALERT", "THERE ARE THREE ANIMATRONICS ADVANCING TOWARDS YOUR LOCATION")
button = Button(root, text="press this if u hate urself", command=msg)
button.place(x=40, y=80)
root.mainloop()