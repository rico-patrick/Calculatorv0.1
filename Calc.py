from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Calculator")
window.configure(bg="WHITE")
window.resizable(False, False)



value = StringVar()  # value that appears on the screen/display
svalue = ""  # initial and final value that is executed


# getting and setting values
def input(num, value):
    global svalue
    svalue = svalue + str(num)
    value.set(svalue)


# operations
def operate(value):
    global svalue
    try:
        result = str(eval(svalue))
        value.set(result)
        history.insert(END, svalue + " = " + result)
        svalue = ""
    except ZeroDivisionError:
        svalue = ""
        value.set("Zero Error")
    except (SyntaxError, AttributeError, TypeError, IndexError):
        svalue = ""
        messagebox.showerror("Error Occupied", "Please Try a Valid Input")
        value.set(svalue)
    # clear function
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

# History
label = Label(window, text="History", width=45, font="Arial")
label.place(x=0, y=305)

history = Listbox(window, height=3, font="Helvetica", width=44, fg="BLACK", bg="WHITE")
history.place(x=0, y=333)

scroll = Scrollbar(window)
scroll.pack(side=LEFT)
class Frame:
    # DisplayBar
    display = Entry(window, bd=3, width=400, font="Helvetica 30", fg="BLACK", bg="WHITE", textvariable=value)
    display.pack()
    """===============================================Buttons================================================"""
    # Operations
    btnadd = Button(window, text="+", font="Verdana 10 bold", bg="GREY", fg="WHITE", command=lambda: input("+", value))
    btndiv = Button(window, text="/", font="Verdana 10 bold", bg="GREY", fg="WHITE", command=lambda: input("/", value))
    btnmul = Button(window, text="X", font="Verdana 10 bold", bg="GREY", fg="WHITE", command=lambda: input("*", value))
    btnsub = Button(window, text="-", font="Verdana 10 bold", bg="GREY", fg="WHITE", command=lambda: input("-", value))
    # Clear
    btnclr = Button(window, text="AC", font="Verdana 10 bold", fg="WHITE", bg="RED", command=lambda: clear())
    btndlt = Button(window, text="Del", font="Verdana 10 bold", bg="GREY", fg="WHITE", command=lambda: delt(value))
    # Result
    btneql = Button(window, text="=", font="Verdana 10 bold", bg="BLUE", fg="WHITE", command=lambda: operate(value))
    # Float
    btndot = Button(window, text=".", font="Verdana 10 bold", fg="WHITE", bg="GREY", command=lambda: input(".", value))
    # Brackets
    btnbo = Button(window, text="(", font="Verdana 10 bold", fg="WHITE", bg="GREY", command=lambda: input("(", value))
    btnbc = Button(window, text=")", font="Verdana 10 bold", fg="WHITE", bg="GREY", command=lambda: input(")", value))
    # Numbers
    btn7 = Button(window, text="7", bg="LIGHT GREY", command=lambda: input(7, value))
    btn8 = Button(window, text="8", bg="LIGHT GREY", command=lambda: input(8, value))
    btn9 = Button(window, text="9", bg="LIGHT GREY", command=lambda: input(9, value))
    btn4 = Button(window, text="4", bg="LIGHT GREY", command=lambda: input(4, value))
    btn5 = Button(window, text="5", bg="LIGHT GREY", command=lambda: input(5, value))
    btn6 = Button(window, text="6", bg="LIGHT GREY", command=lambda: input(6, value))
    btn1 = Button(window, text="1", bg="LIGHT GREY", command=lambda: input(1, value))
    btn2 = Button(window, text="2", bg="LIGHT GREY", command=lambda: input(2, value))
    btn3 = Button(window, text="3", bg="LIGHT GREY", command=lambda: input(3, value))
    btn0 = Button(window, text="0", bg="LIGHT GREY", command=lambda: input(0, value))

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
    btnbo.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=60)
    btnbc.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=60)
    btndlt.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=60)
    btnclr.place(bordermode=OUTSIDE, height=40, width=85, x=295, y=60)

    btn7.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=110)
    btn8.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=110)
    btn9.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=110)
    btndiv.place(bordermode=OUTSIDE, height=40, width=85, x=295, y=110)

    btn4.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=160)
    btn5.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=160)
    btn6.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=160)
    btnmul.place(bordermode=OUTSIDE, height=40, width=85, x=295, y=160)

    btn1.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=210)
    btn2.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=210)
    btn3.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=210)
    btnsub.place(bordermode=OUTSIDE, height=40, width=85, x=295, y=210)

    btndot.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=260)
    btn0.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=260)
    btneql.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=260)
    btnadd.place(bordermode=OUTSIDE, height=40, width=85, x=295, y=260)

obj = Frame()
window.mainloop()
