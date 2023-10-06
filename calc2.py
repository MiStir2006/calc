#imports
from tkinter import *
import math
import tkinter as tk
from tkinter import ttk

#tkinter


window = Tk()
window.title("Calculator")
window.geometry("555x975")
window.resizable(0,0)

#variables
var1:float=-1
var2:float=-1
op=None

#def
def number_button(number:int):
    def p():
        global var1
        global var2
        
        
        if op==None:
            if var1!=-1:
                var1=var1*10+number
            elif var1==-1:
                var1=number
            calculations.config(text=str(var1))
        elif op!=None:
            if var2!=-1:
                var2=var2*10+number
            elif var2==-1:
                var2=number
            calculations.config(text=str(var2))
        print(var1)
        print(var2)
    return p

def oplus():
    global op
    if op==None:
        print("+")
        op="+"
    

def ominus():
    global op
    if op==None:
        print("-")
        op="-"

def otimes():
    global op
    if op==None:
        print("*")
        op="*"

def odiv():
    global op
    if op==None:
        print("/")
        op="/"

def clear():
    global var1
    global var2
    global op
    var1=-1
    var2=-1
    op=None
    calculations.config(text=0)

def endCalc():
    global var1
    global var2
    print("=")
    if var2!=-1:
        if op=="+":
            var1=eval("var1 + var2")
        elif op=="-":
            var1=eval("var1 - var2")
        elif op=="*":
            var1=eval("var1 * var2")
        elif op=="/":
            var1=eval("var1 / var2")
        calculations.config(text=var1)
    else:
        calculations.config(text="Syntax-Error")
    print(var1)
    var2=-1

    


#buttons

zero = Button(
    window, text="0",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(0))

one = Button(
    window, text = "1",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(1))

two = Button(
    window, text="2",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(2))

three = Button(
    window, text="3",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(3))

four = Button(
    window, text="4",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(4))

five = Button(
    window, text="5",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(5))

six = Button(
    window, text="6",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(6))

seven = Button(
    window, text="7",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(7))

eight = Button(
    window, text="8",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(8))

nine = Button(
    window, text="9",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75,
    command = number_button(9))

plus = Button(
    window, text="+"
    ,command = oplus
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)

minus = Button(
    window, text="-"
    ,command = ominus
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)

times = Button(
    window, text="x"
    ,command = otimes
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)

c = Button(
    window, text="C"
    ,command = clear
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)

end_Calc = Button(
    window, text="="
    ,command = endCalc
    ,bg='blue',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)
div = Button(
    window, text="/"
    ,command = odiv
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=55,
    pady=75)
#header
calculations = ttk.Label(
    window, text=0
    
    ,foreground='black'
    ,font=('Arial',25)
    
    ,anchor=E, justify="right"
    )

#grid
calculations.grid(column=4, row=1, sticky=tk.E, pady=75)
one.grid(row=2, column=1)
two.grid(row=2, column=2)
three.grid(row=2, column=3)
plus.grid(row=2, column=4)
four.grid(row=3, column=1)
five.grid(row=3, column=2)
six.grid(row=3, column=3)
minus.grid(row=3, column=4)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
times.grid(row=4, column=4)
c.grid(row=5, column=1)
zero.grid(row=5, column=2)
end_Calc.grid(row=5, column=3)
div.grid(row=5, column=4)


#mainloop
window.mainloop()