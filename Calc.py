from tkinter import *

window = Tk()
window.geometry("400x500")
window.title("Calculator")
window.configure(bg="LIGHT GREY")
label = Label(window, text="Helo", width=400, height=3, justify=RIGHT, fg="BLACK", bg="WHITE")
label.pack()
button = Button(text="7", height=2, width=100)
button_frame.columncon
button.grid(row=0, column=0)
button.pack()
window.mainloop()
