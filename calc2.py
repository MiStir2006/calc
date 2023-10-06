#imports
import math
from tkinter import *
import tkinter as tk
from tkinter import ttk

#tkinter
x:int=300
y:int=600

window = Tk()
window.title("Calculator")
window.geometry(f"{x}x{y}")
window.resizable(0,0)

#variables
var1:list=[]
var2:list=[]
com1:float=-1
com2:float=-1
op=None

#def

#numbers -----------------------------------------------------------------------------------------------------------------------
def number_button(number:int):
    def p():
        global var1
        global var2
        
        c=""
        if op==None:
            var1.append(number)
    
            for i in range (len(var1)):
                c=c+str(var1[i])
            calculations.config(text=str(c))
            print(c)

        elif op!=None:
            var2.append(number)
            
            for i in range (len(var2)):
                c=c+str(var2[i])
            calculations.config(text=str(c))
            print(c)
            calculations.config(text=str(var2))
        print(var1)
        print(var2)
    return p

#plus
def oplus():
    global op
    if op==None:
        print("+")
        op="+"
    
#minus
def ominus():
    global op
    if op==None:
        print("-")
        op="-"
#times
def otimes():
    global op
    if op==None:
        print("*")
        op="*"

#divide by
def odiv():
    global op
    if op==None:
        print("/")
        op="/"

#clear
def clear():
    global var1
    global var2
    global op
    var1=[]
    var2=[]
    op=None
    calculations.config(text=0)

#=
def endCalc():
    global var1
    global var2
    global com1
    global com2
    global op
    print("=")
    ir1=False
    ir2=False
    if var1[0]==math.pi:
        com1=math.pi
        ir1 = True
    if var2[0]==math.pi:
        com2=math.pi
        ir2 = True
    if var1[0]==math.e:
        com1=math.e
        ir1 = True
    if var2[0]==math.e:
        com2=math.e
        ir2 = True
    if var2!=[]:
        
        if ir1!=True:
            c=""
            if len(var1)>=11:
                while len(var1)>=11:
                    var1.remove[11]
            for i in range (len(var1)):
                c=c+str(var1[i])
                calculations.config(text=str(c))
                print(c)
                com1=float(c)
        if ir2!=True:
            c=""
            if len(var2)>=11:
                while len(var2)>=11:
                    var2.remove[11]
            for i in range (len(var2)):
                c=c+str(var2[i])
                calculations.config(text=str(c))
                print(c)
                com2=float(c)
    if op=="+":
        com1=eval("com1 + com2")
    elif op=="-":
        com1=eval("com1 - com2")
    elif op=="*":
        com1=eval("com1 * com2")
    elif op=="/":
        com1=eval("com1 / com2")
    
    else:
        calculations.config(text="Syntax-Error - missing second argument")
        com1=""
        var1=[]
    if com1!="":
        calculations.config(text=com1)
        var1=var1+var2
        
    op=None
    var2=[]
#pi
def cake():
    global var1
    global var2
    global op
    if var1==[]:
        var1=[math.pi]
    elif var1!=[]:
        op="*"
        var2=math.pi
    calculations.config(text="π")

#e
def wwe():
    global var1
    global var2
    global op
    if var1==[]:
        var1=[math.e]
    elif var1!=[]:
        op="*"
        var2=math.pi
    calculations.config(text="e")

#point
def comma():
    print("hi")

#backspace
def back():
    print("backspace")


#buttons ---------------------------------------------------------------------------------------------------------------------------------

zero = Button(
    window, text="0",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(0))

one = Button(
    window, text = "1",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(1))

two = Button(
    window, text="2",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(2))

three = Button(
    window, text="3",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(3))

four = Button(
    window, text="4",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(4))

five = Button(
    window, text="5",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(5))

six = Button(
    window, text="6",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(6))

seven = Button(
    window, text="7",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(7))

eight = Button(
    window, text="8",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(8))

nine = Button(
    window, text="9",
    bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15),
    command = number_button(9))

plus = Button(
    window, text="+"
    ,command = oplus
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

minus = Button(
    window, text="-"
    ,command = ominus
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

times = Button(
    window, text="x"
    ,command = otimes
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

c = Button(
    window, text="C"
    ,command = clear
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

end_Calc = Button(
    window, text="="
    ,command = endCalc
    ,bg='blue',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

div = Button(
    window, text="/"
    ,command = odiv
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

pi = Button(
    window, text="π"
    ,command = cake
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

e = Button(
    window, text="e"
    ,command = wwe
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

point = Button(
    window, text="."
    ,command = comma
    ,bg='black',
    fg='white',
    font=('Arial',25),
    padx=int(x/15),
    pady=int(x/15))

delete = Button(
    window, text="←"
    ,command = "back"
    ,bg='black',
    fg='red',
    font=('Arial',20),
    padx=int(x/15),
    pady=int(x/15))

#header
calculations = ttk.Label(
    window, text=0
    
    ,foreground='black'
    ,font=('Arial',25)
    
    ,anchor=E, justify="right"
    )

#grid
calculations.grid(column=4, row=1, sticky=tk.E, pady=int(x/10))
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
pi.grid(row=6, column=1)
e.grid(row=6, column=2)
point.grid(row=6, column=3)
delete.grid(row=6, column=4)


#mainloop
window.mainloop()