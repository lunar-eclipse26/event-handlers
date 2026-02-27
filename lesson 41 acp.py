from tkinter import *
def convert():
    try:
        inches=float(entry.get())
        cm=inches*2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Enter a valid number")
window=Tk()
window.title("Inches to CM Converter")
window.geometry("300x200")
Label(window,text="Enter length in inches:").pack(pady=5)
entry=Entry(window)
entry.pack(pady=5)
Button(window,text="Convert",command=convert).pack(pady=10)
result_label=Label(window,text="")
result_label.pack(pady=5)
window.mainloop()