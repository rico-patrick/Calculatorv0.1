from _curses import window
from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("Calculator")
window.configure(bg="WHITE")

value = StringVar()  # value that appears on the screen/display
svalue=""            # initial and final value that is executed
def input(num,value):
        global svalue
        svalue = svalue+str(num)
        value.set(svalue)
def operate(value):
        global svalue
        try:
                result=str(eval(svalue))
                value.set(result)
        except ZeroDivisionError:
                svalue=""
                value.set("Math Error")

# clear function
def clear():
        global svalue
        svalue = ""
        value.set(svalue)


class Frame:
        # DisplayBar
        display = Entry(window, bd=3, font="Helvetica 25", fg="BLACK", bg="WHITE", textvariable=value)
        display.pack()
        """===============================Buttons================================="""
        # Operations
        btnadd = Button(window, text="+", bg="GREY")
        btndiv = Button(window, text="/", bg="GREY")
        btnmul = Button(window, text="X", bg="GREY")
        btnsub = Button(window, text="-", bg="GREY")
        btnper = Button(window, text="%", bg="GREY")
        # Clear
        btnclr = Button(window, text="AC", fg="WHITE", bg="RED", command=lambda: clear())

        # Result
        btneql = Button(window, text="=", bg="BLUE", fg="WHITE")
        # Float
        btndot = Button(window, text=".", bg="GREY", command=lambda: input(".", value))
        #Brackets
        btnbo = Button(window, text="(", bg="GREY")
        btnbc = Button(window, text=")", bg="GREY")
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
        btnper.pack()
        btnbo.pack()
        btnbc.pack()
        btnclr.pack()
        btnadd.pack()
        btnsub.pack()
        btnmul.pack()
        btnbo.place(bordermode=OUTSIDE, height=40, width=85, x=10, y=60)
        btnbc.place(bordermode=OUTSIDE, height=40, width=85, x=105, y=60)
        btnper.place(bordermode=OUTSIDE, height=40, width=85, x=200, y=60)
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

obj= Frame()
window.mainloop()