from tkinter import *
import os
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import math

window = Tk()
window.geometry("390x415+700+100")
window.resizable(0, 0)
window.title("Calculator")
icon = PhotoImage(file="Images/icon.png")
window.iconphoto(False, icon)
imghist = PhotoImage(file="Images/history.png")

# value that appears on the screen/display

value = StringVar()

# initial and final value that is executed

svalue = ""

# variables for radio buttons

theme = IntVar()

modes = IntVar()

displayframe = Frame(window, width=390, height=700)
btn_row1 = Frame(window, width=390, height=40)
btn_row2 = Frame(window, width=390, height=40)
btn_row3 = Frame(window, width=390, height=40)
btn_row4 = Frame(window, width=390, height=40)
btn_row5 = Frame(window, width=390, height=40)

#         btnfg       btnbg     btneqlbg   btnacbg    historyfg    historybg    displaybg   displayfg  hisframebg  hisframefg  windowbg  btnoperationsbg
#           0          1            2         3           4             5             6          7           8            9         10        11
color = [
    ["#ffffff", "#1f45fc", "#59e817", "RED", "#000000", "#e0ffff", "#e0ffff", "#1f45fc", "#1f45fc", "WHITE", "#000000",
     "#165AA6"],
    ["BLACK", "#e5e4e2", "#00DCE3", "RED", "BLACK", "WHITE", "WHITE", "BLACK", "WHITE", "BLACK", "WHITE", "#A6AAAA"],
    ["#ffffff", "#000000", "#39ff14", "RED", "WHITE", "BLACK", "BLACK", "WHITE", "BLACK", "WHITE", "BLACK", "#000000"]]


def mode():
    window.configure(menu=menubar, bg=color[theme.get()][10])
    historyframe.configure(bg=color[theme.get()][8], fg=color[theme.get()][9])
    history.configure(fg=color[theme.get()][4], bg=color[theme.get()][5])

    obj.display.configure(bg=color[theme.get()][6], fg=color[theme.get()][7])
    i = 0
    for i in obj.num_list:
        i.configure(fg=color[theme.get()][0], bg=color[theme.get()][1])

    for i in obj.operators:
        i.configure(fg=color[theme.get()][0], bg=color[theme.get()][11])

    for i in obj.scifi:
        i.configure(fg=color[theme.get()][0], bg=color[theme.get()][11])

    obj.btneql.configure(bg=color[theme.get()][2], fg=color[theme.get()][0])
    obj.btnclr.configure(bg=color[theme.get()][3], fg=color[theme.get()][0])


# getting and setting values

def input(num, value):
    global svalue
    svalue = ""
    svalue = obj.display.get() + str(num)
    value.set(svalue)


# ===============================================operations=========================================================

def fact():
    try:
        result = str(math.factorial(eval(obj.display.get())))
        history.insert(END, obj.display.get() + " !  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def exp():
    try:
        result = str(math.exp(eval(obj.display.get())))
        history.insert(END, "e**" + obj.display.get() + "  =" + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def sin():
    try:

        result = str(math.sin(radians(eval(display.get()))))
        history.insert(END, "sin" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)

def sinh():
    try:

        result = str(math.sinh(radians(eval(display.get()))))
        history.insert(END, "sinh" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def log():
    try:

        result = str(math.log10(eval(obj.display.get())))
        history.insert(END, "log" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def cos():
    try:
        result = str(math.cos(radians(eval(obj.display.get()))))
        history.insert(END, "cos" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)

def cosh():
    try:
        result = str(math.cosh(radians(eval(obj.display.get()))))
        history.insert(END, "cosh" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def per():
    try:
        result = str((eval(obj.display.get())) / 100)
        history.insert(END, "cos" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)

def mod():
    try:
        result = str(math.fabs(float(obj.display.get())))
        history.insert(END, "|" + obj.display.get() + "|  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def tan():
    try:
        result = str(math.tan(radians(eval(obj.display.get()))))
        history.insert(END, "tan" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)

def tanh():
    try:
        result = str(math.tanh(radians(eval(obj.display.get()))))
        history.insert(END, "tanh" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)

def root():
    try:
        result = str(math.sqrt(eval(obj.display.get())))
        history.insert(END, "\u221A" + obj.display.get() + "  =  " + result)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


def pi():
    try:
        result = str(math.pi)
        value.set(result)

    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)


index = 0

def rad():
    global index

    if (index==0):

        obj.btnrad.config(text="\u00B0")
        try:
            result = str(math.degrees(eval(obj.display.get())))
            history.insert(END, obj.display.get() + "\u00B0  =  " + result)
            value.set(result)

        except ZeroDivisionError:
            svalue = ""
            value.set("Zero Error")
        except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
            svalue = ""
            messagebox.showerror("Error Occupied", "Please Try a Valid Input")
            value.set(svalue)

    else:
        obj.btnrad.config(text="\u33AD")
        try:
            result = str(math.radians(eval(obj.display.get())))
            history.insert(END, obj.display.get() + "\u33AD  =  " + result)
            value.set(result)

        except ZeroDivisionError:
            svalue = ""
            value.set("Zero Error")
        except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
            svalue = ""
            messagebox.showerror("Error Occupied", "Please Try a Valid Input")
            value.set(svalue)

    index = not index

def operate(value):
    global svalue

    try:

        result = str(eval(obj.display.get()[:-1].lstrip('0') + obj.display.get()[-1]))
        history.insert(END, obj.display.get() + "  =  " + result)
        value.set(result)
        svalue = ""
    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, NameError, AttributeError, ValueError, TypeError, IndexError):
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

historyframe = LabelFrame(window, text="Recent", font="Arial 12 bold", fg=color[theme.get()][9],
                          bg=color[theme.get()][8])

# ScrollBar

scrollx = Scrollbar(historyframe, orient=HORIZONTAL)
scrolly = Scrollbar(historyframe, orient=VERTICAL)

# Recent List

history = Listbox(historyframe,
                  font="Helvetica 15",
                  height=3,
                  bg=color[theme.get()][5],
                  fg=color[theme.get()][4],
                  xscrollcommand=scrollx.set,
                  yscrollcommand=scrolly.set)

history.bind('<Control-x>', lambda e: 'break')  # disabling cut function in history...

scrollx.config(command=history.xview)
scrolly.config(command=history.yview)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

history.pack(expand=True, fill=BOTH)

displayframe.pack(expand=True, fill=BOTH)

hist = IntVar()


def toggle():
    if hist.get() == 1:
        historyframe.pack(side=BOTTOM, expand=True, fill=BOTH)
    elif hist.get() == 0:
        historyframe.pack_forget()


class Frame:
    # DisplayBar
    btnhist = Checkbutton(displayframe, image=imghist, command=lambda: toggle(), variable=hist, bd=0,
                          activebackground="#ffffff",
                          width=40, bg="White", height=1, borderwidth=0, relief=FLAT)
    display = Entry(displayframe, width=400, bd=0, font=" Arial 30", justify=RIGHT,
                    fg=color[theme.get()][7], bg=color[theme.get()][6],
                    textvariable=value)
    display.focus_set()
    btnhist.pack(side=LEFT, expand=True, fill=BOTH)
    display.pack(expand=True, fill=BOTH)

    # =====================================================Buttons=========================================================

    # Operation Buttons

    # Brackets

    btnbo = Button(btn_row1,
                   text="(",
                   font="Verdana 12 bold",
                   fg=color[theme.get()][0], bg=color[theme.get()][11],
                   relief="groove",
                   width=1,
                   bd=1,
                   highlightthickness=0,
                   command=lambda: input("(", value))

    btnbc = Button(btn_row1, text=")",
                   font="Verdana 12 bold",
                   fg=color[theme.get()][0], bg=color[theme.get()][11],
                   relief="groove",
                   width=1,
                   bd=1,
                   highlightthickness=0,
                   command=lambda: input(")", value))

    btnpwr = Button(btn_row1,
                    text="x\u207f",
                    font="Verdana 12 bold",
                    width=1,
                    bd=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input("**", value))

    btnfact = Button(btn_row1,
                     text="n!",
                     font="Verdana 12 bold",
                     width=1,
                     bd=1,
                     bg=color[theme.get()][11], fg=color[theme.get()][0],
                     relief="groove",
                     highlightthickness=0,
                     command=lambda: fact())

    # All Clear And Backspace
    btndlt = Button(btn_row1,
                    text="\u232b",
                    font="Arial_black 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: delt(value))

    btnclr = Button(btn_row1,
                    text="AC",
                    font="Verdana 12 bold",
                    width=1,
                    fg=color[theme.get()][0], bg=color[theme.get()][3],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: clear())

    btnmod = Button(btn_row1,
                    text="|x|",
                    font="Verdana 12 bold",
                    width=1,
                    fg=color[theme.get()][0], bg=color[theme.get()][11],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: mod())

    # Numbers
    btn7 = Button(btn_row2,
                  text="7",
                  font="Verdana 12 bold",
                  width=2,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(7, value))

    btn8 = Button(btn_row2,
                  text="8",
                  font="Verdana 12 bold",
                  width=2,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(8, value))

    btn9 = Button(btn_row2,
                  text="9",
                  font="Verdana 12 bold",
                  width=2,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(9, value))

    btndiv = Button(btn_row2,
                    text="\u00f7",
                    font="Verdana 12 bold",
                    width=2,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input("/", value))
    btnexp = Button(btn_row2,
                    text="e",
                    font="Verdana 12 bold",
                    width=2,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: exp())
    btnsin = Button(btn_row2,
                    text="sin",
                    font="Verdana 12 bold",
                    width=2,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: sin())

    btnsinh = Button(btn_row2,
                     text="sinh",
                     font="Verdana 12 bold",
                     width=2,
                     bg=color[theme.get()][11], fg=color[theme.get()][0],
                     relief="groove",
                     highlightthickness=0,
                     command=lambda: sinh())

    btn4 = Button(btn_row3,
                  text="4",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(4, value))

    btn5 = Button(btn_row3,
                  text="5",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(5, value))

    btn6 = Button(btn_row3,
                  text="6",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(6, value))

    btnmul = Button(btn_row3,
                    text="\u00d7",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input("*", value))
    btnlog = Button(btn_row3,
                    text="log",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: log())
    btncos = Button(btn_row3,
                    text="cos",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: cos())

    btncosh = Button(btn_row3,
                     text="cosh",
                     font="Verdana 12 bold",
                     width=1,
                     bg=color[theme.get()][11], fg=color[theme.get()][0],
                     relief="groove",
                     highlightthickness=0,
                     command=lambda: cosh())

    btn1 = Button(btn_row4,
                  text="1",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(1, value))

    btn2 = Button(btn_row4,
                  text="2",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(2, value))

    btn3 = Button(btn_row4,
                  text="3",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(3, value))

    btnsub = Button(btn_row4,
                    text="-",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input("-", value))
    btnper = Button(btn_row4,
                    text="%",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: per())
    btntan = Button(btn_row4,
                    text="tan",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: tan())

    btntanh = Button(btn_row4,
                     text="tanh",
                     font="Verdana 12 bold",
                     width=1,
                     bg=color[theme.get()][11], fg=color[theme.get()][0],
                     relief="groove",
                     highlightthickness=0,
                     command=lambda: tanh())

    # Float
    btndot = Button(btn_row5,
                    text=".",
                    font="Verdana 12 bold",
                    width=1,
                    fg=color[theme.get()][0], bg=color[theme.get()][11],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input(".", value))

    btn0 = Button(btn_row5,
                  text="0",
                  font="Verdana 12 bold",
                  width=1,
                  bg=color[theme.get()][1],
                  fg=color[theme.get()][0],
                  relief="groove",
                  highlightthickness=0,
                  command=lambda: input(0, value))

    # Result
    btneql = Button(btn_row5,
                    text="=",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][2], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: operate(value))

    # Enter Key for equal button

    window.bind("<KP_Enter>", enterkey)
    window.bind("<Return>", enterkey)

    btnadd = Button(btn_row5,
                    text="+",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: input("+", value))
    btnroot = Button(btn_row5,
                     text="\u221A",
                     font="Verdana 12 bold",
                     width=1,
                     bg=color[theme.get()][11], fg=color[theme.get()][0],
                     relief="groove",
                     highlightthickness=0,
                     command=lambda: root())
    btnpi = Button(btn_row5,
                   text="\u03C0",
                   font="Verdana 12 bold",
                   width=1,
                   bg=color[theme.get()][11], fg=color[theme.get()][0],
                   relief="groove",
                   highlightthickness=0,
                   command=lambda: pi())

    btnrad = Button(btn_row5,
                    text="\u33AD",
                    font="Verdana 12 bold",
                    width=1,
                    bg=color[theme.get()][11], fg=color[theme.get()][0],
                    relief="groove",
                    highlightthickness=0,
                    command=lambda: rad())

    btnbo.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btnbc.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btnclr.pack(side=RIGHT, expand=True, fill=BOTH, ipadx=2)
    btndlt.pack(side=RIGHT, expand=True, fill=BOTH, ipadx=2)

    btn7.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn8.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn9.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btndiv.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)

    btn4.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn5.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn6.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btnmul.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)

    btn1.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn2.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn3.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btnsub.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)

    btndot.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btn0.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btneql.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)
    btnadd.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)

    btn_row1.pack(expand=True, fill=BOTH)
    btn_row2.pack(expand=True, fill=BOTH)
    btn_row3.pack(expand=True, fill=BOTH)
    btn_row4.pack(expand=True, fill=BOTH)
    btn_row5.pack(expand=True, fill=BOTH)

    num_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0]

    operators = [btndiv, btndlt, btnbo, btnbc, btnadd, btnsub, btnmul, btndot]

    scifi = [btnpi, btnroot, btnpwr, btnper, btnlog, btnfact, btnexp, btntan, btnsin, btncos,btntanh, btnsinh, btncosh,btnmod, btnrad]

    def standard(self):
        window.geometry("390x415")
        for i in obj.scifi:
            i.forget()

    def scientific(self):
        window.geometry("535x390")

        for i in obj.scifi:
            i.pack(side=LEFT, expand=True, fill=BOTH, ipadx=2)


obj = Frame()

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

mode = Menu(menubar, tearoff=0)
mode.add_radiobutton(label="Standard", variable=modes, value=0, command=obj.standard)
mode.add_radiobutton(label="Scientific", variable=modes, value=1, command=obj.scientific)
menubar.add_cascade(label="Mode", menu=mode)

help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=lambda: about())
menubar.add_cascade(label="Help", menu=help)

window.configure(menu=menubar, bg=color[theme.get()][10])

# Close When Escape key is pressed

window.bind("<Escape>", escapekey)

window.mainloop()
