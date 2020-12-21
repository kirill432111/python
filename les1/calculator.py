import tkinter
from tkinter import *


def one():
    return schet.set(schet.get() + '1')
def two():
    return schet.set(schet.get() + '2')
def three():
    return schet.set(schet.get() + '3')
def four():
    return schet.set(schet.get() + '4')
def five():
    return schet.set(schet.get() + '5')
def six():
    return schet.set(schet.get() + '6')
def seven():
    return schet.set(schet.get() + '7')
def eight():
    return schet.set(schet.get() + '8')
def nine():
    return schet.set(schet.get() + '9')
def zero():
    return schet.set(schet.get() + '0')
def plus():
    return schet.set(schet.get() + '+')
def minus():
    return schet.set(schet.get() + '-')
def step():
    return schet.set(schet.get() + '**')
def left():
    return schet.set(schet.get() + '(')
def right():
    return schet.set(schet.get() + ')')
def multi():
    return schet.set(schet.get() + '*')
def drob():
    return schet.set(schet.get() + '/')
def proc():
    return schet.set(schet.get() + '/100')
def toch():
    return schet.set(schet.get() + '.')
def vse():
    return schet.set('')
def ravno():
    return schet.set(eval(schet.get()))



window = tkinter.Tk()
window.title("Calculator")

window.geometry('193x280+90+0')

schet = StringVar()

pole = Entry(window, width=50, font='Arial 30', textvariable=schet,bg="#000", foreground="#FFF")
pole.pack()


knopka1 = Button(window, text=' ', width=6, height=1)
knopka1.place(x=0, y=120)
knopka2 = Button(window, text=' ', width=6, height=1)
knopka2.place(x=47, y=120)
knopka3 = Button(window, text=' % ', width=6, command = proc, height=1,bg="#000",foreground="#FFF")
knopka3.place(x=94, y=120)
knopka4 = Button(window, text=' ( ', width=6, command = left, height=1,bg="#000",foreground="#FFF")
knopka4.place(x=0, y=147)
knopka5 = Button(window, text=' ) ', width=6, command = right, height=1,bg="#000",foreground="#FFF")
knopka5.place(x=47, y=147)
knopka6 = Button(window, text=' ^x ', width=6, command = step, height=1,bg="#000",foreground="#FFF")
knopka6.place(x=94, y=147)
knopka7 = Button(window, text=' 1 ', command = one, width=6, height=1,bg="#000",foreground="#FFF")
knopka7.place(x=0, y=174)
knopka8 = Button(window, text=' 2 ', command = two, width=6, height=1,bg="#000",foreground="#FFF")
knopka8.place(x=47, y=174)
knopka9 = Button(window, text=' 3 ', width=6, command = three, height=1,bg="#000",foreground="#FFF")
knopka9.place(x=94, y=174)
knopka10 = Button(window, text=' 4 ', width=6, command = four, height=1,bg="#000",foreground="#FFF")
knopka10.place(x=0, y=201)
knopka11 = Button(window, text=' 5 ', width=6, command = five, height=1,bg="#000",foreground="#FFF")
knopka11.place(x=47, y=201)
knopka12 = Button(window, text=' 6 ', width=6, command = six, height=1,bg="#000",foreground="#FFF")
knopka12.place(x=94, y=201)
knopka13 = Button(window, text=' 7 ', width=6, command = seven, height=1,bg="#000",foreground="#FFF")
knopka13.place(x=0, y=228)
knopka14 = Button(window, text=' 8 ', width=6, command = eight, height=1,bg="#000",foreground="#FFF")
knopka14.place(x=47, y=228)
knopka15 = Button(window, text=' 9 ', width=6, command = nine, height=1,bg="#000",foreground="#FFF")
knopka15.place(x=94, y=228)
knopka16 = Button(window, text=' ', width=6, height=1,bg="#000",foreground="#FFF")
knopka16.place(x=0, y=255)
knopka17 = Button(window, text=' 0 ', width=6, command = zero, height=1,bg="#000",foreground="#FFF")
knopka17.place(x=47, y=255)
knopka18 = Button(window, text=' . ', width=6, command = toch, height=1,bg="#000",foreground="#FFF")
knopka18.place(x=94, y=255)
knopka19 = Button(window, text=' CE ', width=6, command = vse, height=1,bg="#000",foreground="#FFF")
knopka19.place(x=141, y=120)
knopka20 = Button(window, text=' / ', width=6, command = drob, height=1,bg="#000",foreground="#FFF")
knopka20.place(x=141, y=147)
knopka21 = Button(window, text=' х ', width=6, command = multi, height=1,bg="#000",foreground="#FFF")
knopka21.place(x=141, y=174)
knopka22 = Button(window, text=' - ', width=6, command = minus, height=1,bg="#000",foreground="#FFF")
knopka22.place(x=141, y=201)
knopka23 = Button(window, text=' + ', width=6, command = plus, height=1,bg="#000",foreground="#FFF")
knopka23.place(x=141, y=228)
knopka24 = Button(window, text=' = ', width=6, command = ravno, height=1,bg="#000",foreground="#FFF")
knopka24.place(x=141, y=255)



window.mainloop()