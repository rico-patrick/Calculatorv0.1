from tkinter import *
import os
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

window = Tk()
window.geometry("390x415+700+100")
window.resizable(0, 0)
window.title("Calculator")
photo = PhotoImage(file="Images/icon.png")
window.iconphoto(False, photo)

# value that appears on the screen/display

value = StringVar()

# initial and final value that is executed

svalue = ""

# themes
theme = IntVar()

#         btnfg       btnbg     btneqlbg   btnacbg    historyfg    historybg displaybg   displayfg  hisframebg  hisframefg  windowbg
#           0          1            2       3           4             5         6          7           8         9            10
color = [["#FFFFFF", "#4a8fe4", "#3fd991", "RED",     "#4169E1",   "WHITE",  "WHITE",   "#4169E1", "#7ef9ff", "WHITE",     "#4a8fe4"],
         ["BLACK",   "WHITE",   "#3b5998", "RED",      "BLACK",    "WHITE",   "WHITE",    "BLACK",   "WHITE", "BLACK",       "WHITE"],
         ["WHITE",  "#1a3f4b",  "#39ff14", "RED",      "WHITE",   "BLACK",    "BLACK",    "WHITE",   "BLACK", "WHITE",         "BLACK"]]


def mode():
    window.configure(menu=menubar, bg=color[theme.get()][10])
    frame.configure(bg=color[theme.get()][8], fg=color[theme.get()][9])
    history.configure(fg=color[theme.get()][4], bg=color[theme.get()][5])

    obj.display.configure(bg=color[theme.get()][6], fg=color[theme.get()][7])
    i = 0
    for i in obj.num_list:
        i.configure(fg=color[theme.get()][0], bg=color[theme.get()][1])

    for i in obj.operators:
        i.configure(fg=color[theme.get()][0], bg=color[theme.get()][1])

    obj.btneql.configure(bg=color[theme.get()][2], fg=color[theme.get()][0])
    obj.btnclr.configure(bg=color[theme.get()][3], fg=color[theme.get()][0])

# getting and setting values

def input(num, value):
    global svalue
    svalue = ""
    svalue = obj.display.get() + str(num)
    value.set(svalue)


# ===============================================operations=========================================================

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

"""==============================================Methods for menu==============================================="""


# Help menu

def about():
    if sys.platform == 'linux':
        os.system('xdg-open "readme.txt"')  # Opening readme file from
    else:
        os.system('start "readme.txt"')


# File menu functions

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


# Restarts the current program

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Frame for recent_operations

frame = LabelFrame(window, text="Recent", font="Arial 12 bold", fg=color[theme.get()][9], bg=color[theme.get()][8])

# ScrollBar

scrollx = Scrollbar(frame, orient=HORIZONTAL)
scrolly = Scrollbar(frame, orient=VERTICAL)

# Recent List

history = Listbox(frame,
                  height=4,
                  font="Helvetica 11",
                  width=46,
                  bg=color[theme.get()][5],
                  fg=color[theme.get()][4],
                  xscrollcommand=scrollx.set,
                  yscrollcommand=scrolly.set)

history.bind('<Control-x>', lambda e: 'break')  # disabling cut function in history...

scrollx.config(command=history.xview)
scrolly.config(command=history.yview)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

history.pack()

frame.place(x=0, y=305)

"""=======================================================Menu bar================================================"""

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

view = Menu(menubar, tearoff=0)

view.add_radiobutton(label="Default", variable=theme, value=0, command=mode)
view.add_radiobutton(label="Light", variable=theme, value=1, command=mode)
view.add_radiobutton(label="Dark", variable=theme, value=2, command=mode)

menubar.add_cascade(label="View", menu=view)

help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=lambda: about())
menubar.add_cascade(label="Help", menu=help)

window.configure(menu=menubar, bg=color[theme.get()][10])

class Frame:
    # DisplayBar

    display = Entry(window, bd=3, width=400, font=" Arial 30", justify=RIGHT,
                    fg=color[theme.get()][7], bg=color[theme.get()][6],
                    textvariable=value)
    display.focus_set()
    display.pack()

    # =====================================================Buttons=========================================================

    # Operation Buttons

    btnadd = Button(window,
                    text="+",
                    font="Verdana 10 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input("+", value))

    btndiv = Button(window,
                    text="\u00f7",
                    font="Verdana 11 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input("/", value))

    btnmul = Button(window,
                    text="\u00d7",
                    font="Verdana 10 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input("*", value))

    btnsub = Button(window,
                    text="-",
                    font="Verdana 10 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input("-", value))

    btnsqr = Button(window,
                    text="x\u00b2",
                    font="Verdana 10 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input("**2", value))

    # All Clear And Backspace

    btnclr = Button(window,
                    text="AC",
                    font="Verdana 10 bold",
                    fg=color[theme.get()][0], bg=color[theme.get()][3],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: clear())

    btndlt = Button(window,
                    text="\u232b",
                    font="Arial_black 11 bold",
                    bg=color[theme.get()][1], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: delt(value))

    # Result
    btneql = Button(window,
                    text="=",
                    font="Verdana 10 bold",
                    bg=color[theme.get()][2], fg=color[theme.get()][0],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: operate(value))

    # Enter Key for equal button

    window.bind("<KP_Enter>", enterkey)
    window.bind("<Return>", enterkey)

    # Float
    btndot = Button(window,
                    text=".",
                    font="Verdana 10 bold",
                    fg=color[theme.get()][0], bg=color[theme.get()][1],
                    relief="flat",
                    highlightthickness=0,
                    command=lambda: input(".", value))

    # Brackets

    btnbo = Button(window,
                   text="(",
                   font="Verdana 10 bold",
                   fg=color[theme.get()][0], bg=color[theme.get()][1],
                   relief="flat",
                   highlightthickness=0,
                   command=lambda: input("(", value))

    btnbc = Button(window, text=")",
                   font="Verdana 10 bold",
                   fg=color[theme.get()][0], bg=color[theme.get()][1],
                   relief="flat",
                   highlightthickness=0,
                   command=lambda: input(")", value))

    # Numbers
    btn7 = Button(window,
                  text="7",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(7, value))

    btn8 = Button(window,
                  text="8",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(8, value))

    btn9 = Button(window,
                  text="9",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(9, value))

    btn4 = Button(window,
                  text="4",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(4, value))

    btn5 = Button(window,
                  text="5",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(5, value))

    btn6 = Button(window,
                  text="6",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(6, value))

    btn1 = Button(window,
                  text="1",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(1, value))

    btn2 = Button(window,
                  text="2",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(2, value))

    btn3 = Button(window,
                  text="3",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(3, value))

    btn0 = Button(window,
                  text="0",
                  font="Verdana 10 bold",
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="flat",
                  highlightthickness=0,
                  command=lambda: input(0, value))

    # Button Formats, Position And Packing
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
    btnsqr.pack()

    btnbo.place(bordermode=OUTSIDE,
                height=40,
                width=40,
                x=10, y=60)

    btnbc.place(bordermode=OUTSIDE,
                height=40,
                width=40,
                x=55, y=60)

    btnsqr.place(bordermode=OUTSIDE,
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
    num_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btndot]

    operators = [btndiv, btndlt, btnbo, btnbc, btnadd, btnsub, btnmul, btnsqr]


obj = Frame()

# Close When Escape key is pressed

window.bind("<Escape>", escapekey)

window.mainloop()
