from tkinter import *
import os
from tkinter import messagebox, Frame
from tkinter.filedialog import asksaveasfilename, asksaveasfile
from tkinter.font import Font

window = Tk()
window.geometry("390x415+700+100")
window.title("Calculator")
photo = PhotoImage(file="Images/icon.png")
window.iconphoto(False, photo)

# value that appears on the screen/display
value = StringVar()
# initial and final value that is executed

svalue = ""


# getting and setting values
def input(num, value):
    global svalue
    svalue = ""
    svalue = obj.display.get() + str(num)
    value.set(svalue)


# operations
def operate(value):
    global svalue
    try:

        result = str(eval(obj.display.get()))
        history.insert(END, obj.display.get() + "  =  " + result)
        value.set(result)
        svalue = ""
    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, AttributeError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)
    # clear function


# Clear function
def clear():
    global svalue
    svalue = ""
    value.set(svalue)


# backspace function
def delt(value):
    global svalue
    temp = svalue
    temp = temp[0:-1]
    svalue = temp
    value.set(svalue)


# Key Event Functions
def enterkey(event):
    operate(value)


def escapekey(event):
    on_Closing()


# Window Closing
def on_Closing():
    if messagebox.askokcancel("Quit!!", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_Closing)


# Restarts the current program
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# File menu functions

# Opening readme file from
def about():
    if sys.platform == 'linux':
        os.system('xdg-open "readme.txt"')  # works for urls too
    else:
        os.system('start "readme.txt"')


# Save
def save():
    files = [('All Files', '*.*'),
             ('Text Document', '*.txt')]

    file = asksaveasfile(mode='w', filetypes=files, initialfile=".txt", defaultextension=files)

    if file is None:
        return

    for x in range(history.size()):
        file_to_save = str(history.get(x) + "\n")
        file.write(file_to_save)
    file.close()


frame = LabelFrame(window, text="Recent", font="Arial 12 bold", bg="WHITE")

# ScrollBar
scrollx = Scrollbar(frame, orient=HORIZONTAL)
scrolly = Scrollbar(frame, orient=VERTICAL)

# History List
history = Listbox(frame,
                  height=4,
                  font="Helvetica 11",
                  width=46,
                  fg="BLACK",
                  bg="WHITE",
                  xscrollcommand=scrollx.set,
                  yscrollcommand=scrolly.set)

scrollx.config(command=history.xview)
scrolly.config(command=history.yview)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

history.pack()

frame.place(x=0, y=305)
menubar = Menu(window)
file = Menu(menubar, tearoff=0)
file.add_command(label="New", command=restart_program)
file.add_command(label="Save", command=lambda: save())

file.add_separator()

file.add_command(label="Exit", command=on_Closing)

menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)

edit.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: window.focus_get().event_generate('<<Cut>>'))
edit.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: window.focus_get().event_generate('<<Copy>>'))
edit.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: window.focus_get().event_generate('<<Paste>>'))
edit.add_command(label="Delete List", command=lambda: history.delete(ANCHOR))
menubar.add_cascade(label="Edit", menu=edit)

help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=lambda: about())
menubar.add_cascade(label="Help", menu=help)

window.configure(menu=menubar, bg="WHITE")


class Frame:
    # DisplayBar
    display = Entry(window, bd=3, width=400, font=" Arial 30", justify=RIGHT, fg="BLACK", bg="WHITE",
                    textvariable=value)
    display.pack()
# =================================================Buttons=========================================================

    # Operations
    btnadd = Button(window,
                    text="+",
                    font="Verdana 10 bold",
                    bg="GREY",
                    fg="WHITE",
                    command=lambda: input("+", value))

    btndiv = Button(window,
                    text="\u00f7",
                    font="Verdana 10 bold",
                    bg="GREY",
                    fg="WHITE",
                    command=lambda: input("/", value))

    btnmul = Button(window,
                    text="\u00d7",
                    font="Verdana 10 bold",
                    bg="GREY",
                    fg="WHITE",
                    command=lambda: input("*", value))

    btnsub = Button(window,
                    text="-",
                    font="Verdana 10 bold",
                    bg="GREY", fg="WHITE",
                    command=lambda: input("-", value))

    # Clear
    btnclr = Button(window,
                    text="AC",
                    font="Verdana 10 bold",
                    fg="WHITE",
                    bg="RED",
                    command=lambda: clear())

    btndlt = Button(window,
                    text="\u232b",
                    font="Verdana 10 bold",
                    bg="BLACK",
                    fg="WHITE",
                    command=lambda: delt(value))

    # Result
    btneql = Button(window,
                    text="=",
                    font="Verdana 10 bold",
                    bg="BLUE",
                    fg="WHITE",
                    command=lambda: operate(value))

    # Enter Key instead of equal button
    window.bind("<KP_Enter>", enterkey)
    window.bind("<Return>", enterkey)

    # Float
    btndot = Button(window,
                    text=".",
                    font="Verdana 10 bold",
                    fg="WHITE",
                    bg="GREY",
                    command=lambda: input(".", value))

    # Brackets
    btnbo = Button(window,
                   text="(",
                   font="Verdana 10 bold",
                   fg="WHITE", bg="GREY",
                   command=lambda: input("(", value))

    btnbc = Button(window, text=")",
                   font="Verdana 10 bold",
                   fg="WHITE",
                   bg="GREY",
                   command=lambda: input(")", value))

    # Numbers
    btn7 = Button(window,
                  text="7",
                  bg="LIGHT GREY",
                  command=lambda: input(7, value))

    btn8 = Button(window,
                  text="8",
                  bg="LIGHT GREY",
                  command=lambda: input(8, value))

    btn9 = Button(window,
                  text="9",
                  bg="LIGHT GREY",
                  command=lambda: input(9, value))

    btn4 = Button(window,
                  text="4",
                  bg="LIGHT GREY",
                  command=lambda: input(4, value))

    btn5 = Button(window,
                  text="5",
                  bg="LIGHT GREY",
                  command=lambda: input(5, value))

    btn6 = Button(window,
                  text="6",
                  bg="LIGHT GREY",
                  command=lambda: input(6, value))

    btn1 = Button(window,
                  text="1",
                  bg="LIGHT GREY",
                  command=lambda: input(1, value))

    btn2 = Button(window,
                  text="2",
                  bg="LIGHT GREY",
                  command=lambda: input(2, value))

    btn3 = Button(window,
                  text="3",
                  bg="LIGHT GREY",
                  command=lambda: input(3, value))

    btn0 = Button(window,
                  text="0",
                  bg="LIGHT GREY",
                  command=lambda: input(0, value))

    # Button Formats and Position
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn6.pack()
    btn7.pack()
    btn8.pack()
    btn9.pack()
    btn0.pack()
    btndot.pack()
    btndiv.pack()
    btneql.pack()
    btndlt.pack()
    btnbo.pack()
    btnbc.pack()
    btnclr.pack()
    btnadd.pack()
    btnsub.pack()
    btnmul.pack()

    btnbo.place(bordermode=OUTSIDE,
                height=40,
                width=85,
                x=10, y=60)

    btnbc.place(bordermode=OUTSIDE,
                height=40,
                width=85,
                x=105, y=60)

    btndlt.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=200, y=60)

    btnclr.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=295, y=60)

    btn7.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=10, y=110)

    btn8.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=105, y=110)

    btn9.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=200, y=110)

    btndiv.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=295, y=110)

    btn4.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=10, y=160)

    btn5.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=105, y=160)

    btn6.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=200, y=160)

    btnmul.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=295, y=160)

    btn1.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=10, y=210)

    btn2.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=105, y=210)

    btn3.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=200, y=210)

    btnsub.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=295, y=210)

    btndot.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=10, y=260)

    btn0.place(bordermode=OUTSIDE,
               height=40,
               width=85,
               x=105, y=260)

    btneql.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=200, y=260)

    btnadd.place(bordermode=OUTSIDE,
                 height=40,
                 width=85,
                 x=295, y=260)


obj = Frame()

# Close When Escape key is pressed
window.bind("<Escape>", escapekey)

window.mainloop()
