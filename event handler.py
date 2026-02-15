from tkinter import *
window = Tk()
window.title("Event_handler")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nGRRR_BUTTON_ANGRY")
button = Button(text="press_me_and_i_will_get_angry")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()