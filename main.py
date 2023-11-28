from tkinter import*
import math as math

window = Tk()
window.title("TCG Calculator")
#window.geometry('445x596')

showText = StringVar()
panel = Entry(window, font=("SegoeUI", 30), textvariable = showText, width=21)
panel.grid(columnspan=4)

last_input = len(panel.get())

def press(symbol):
    #panel.insert(END, symbol)
    showText.set(showText.get()+symbol)

def pi():
    p = int(showText.get())
    new = p*3.141592653589793
    showText.set(str(new))#showText.get()+math.pi)

def sqrt():
    s = int(showText.get())
    new = s.sqrt()
    showText.set(str(new))
                 
def clear():
    panel.delete(0, END)

def equals():
    result = eval(showText.get())
    showText.set(str(result))

def delete():
    panel.delete(last_input - 1)

button1 = Button(window, text="1", width=14, height=4, command = lambda:press("1"))
button1.grid(row=1, column=0)
button2 = Button(window, text="2", width=14, height=4, command = lambda:press("2"))
button2.grid(row=1, column=1)
button3 = Button(window, text="3", width=14, height=4, command = lambda:press("3"))
button3.grid(row=1, column=2)
buttonplus = Button(window, text="+", width=14, height=4, command = lambda:press("+"))
buttonplus.grid(row=1, column=3)
button4 = Button(window, text="4", width=14, height=4, command = lambda:press("4"))
button4.grid(row=2, column=0)
button5 = Button(window, text="5", width=14, height=4, command = lambda:press("5"))
button5.grid(row=2, column=1)
button6 = Button(window, text="6", width=14, height=4, command = lambda:press("6"))
button6.grid(row=2, column=2)
buttonminus = Button(window, text="-", width=14, height=4, command = lambda:press("-"))
buttonminus.grid(row=2, column=3)
button7 = Button(window, text="7", width=14, height=4, command = lambda:press("7"))
button7.grid(row=3, column=0)
button8 = Button(window, text="8", width=14, height=4, command = lambda:press("8"))
button8.grid(row=3, column=1)
button9 = Button(window, text="9", width=14, height=4, command = lambda:press("9"))
button9.grid(row=3, column=2)
buttontimes = Button(window, text="*", width=14, height=4, command = lambda:press("*"))
buttontimes.grid(row=3, column=3)
button0 = Button(window, text="0", width=14, height=4, command = lambda:press("0"))
button0.grid(row=4, column=1)
buttonC = Button(window, text="C", width=14, height=4, command = lambda:clear())
buttonC.grid(row=6, column=2)
buttonequals = Button(window, text="=", width=14, height=4, command = lambda:equals())
buttonequals.grid(row=6, column=3)
buttondivide = Button(window, text="/", width=14, height=4, command = lambda:press("/"))
buttondivide.grid(row=4, column=3)
buttondecimal = Button(window, text=".", width=14, height=4, command = lambda:press("."))
buttondecimal.grid(row=4, column=2)
buttonbackspace = Button(window, text="DEL", width=14, height=4, command = lambda:delete())
buttonbackspace.grid(row=5, column=3)
buttonexp = Button(window, text="exp", width=14, height=4, command = lambda:press("**"))
buttonexp.grid(row=5, column=1)
buttonopen = Button(window, text="(", width=14, height=4, command = lambda:press("("))
buttonopen.grid(row=6, column=0)
buttonclose = Button(window, text=")", width=14, height=4, command = lambda:press(")"))
buttonclose.grid(row=6, column=1)
buttonpom = Button(window, text="+/-", width=14, height=4, command = lambda:press("*-1"))
buttonpom.grid(row=4, column=0)
buttonpi = Button(window, text="π", width=14, height=4, command = lambda:pi())
buttonpi.grid(row=5, column=0)

'------------------------------------------------------------------------------'

buttonsqrt = Button(window, text="sqrt", width=14, height=4, command = lambda:sqrt())
buttonsqrt.grid(row=5, column=2)
