from tkinter import *

window = Tk()
window.geometry("400x500")
window.title("Calculator")
button = Button(text="ok", width=30, height=30)
label = Label(window, text="")
label.pack()
button.pack()
window.mainloop()
