from tkinter import *
from tkinter import messagebox as mbox


window = Tk()
window['bg']="black"
window.title("Супер-мега шифровщик")

def rashifr():
    c = txt1.get()
    k = txt2.get()
    d = ""
    for i, j in enumerate(c):
        gg = (ord(j) - ord(k[i]))

        d += chr(gg % 26 + 65)
    mbox.showinfo("Расшифрованное сообщение: ", str(d))
    print(str(d))

def zashifr():
    m = txt1.get()
    k = txt2.get()
    k *= len(m) // len(k) + 1
    c = ""
    for i, j in enumerate(m):
        gg = (ord(j)  + ord(k[i]))
        c += chr(gg % 26 + 65)
    mbox.showinfo("Зашифрованное сообщение: ", str(c))
    print(str(c))

lbl = Label(window, text="Введите текст который нужно зашифровать/расшифровать: ", bg="black", foreground="red")
lbl.place(x=0, y=0)

lb2 = Label(window, text="Введите ключ: ",bg="black",foreground="red")
lb2.place(x=130, y=110)

txt1 = Entry(window,width=30)
txt1.place(x=80, y=20)

txt2 = Entry(window,width=30)
txt2.place(x=80, y=130)

btn_zash = Button(window, text="зашифровать!", bg="grey",foreground="black", command = zashifr)
btn_zash.place(x=30, y=230)

btn_rash = Button(window, text="Взломать\nсупер-мега зашифрованный\nтекст!",bg="grey",foreground="black", command = rashifr)
btn_rash.place(x=150, y=220)


lbl3= Label(window, text="ВАЖНО: \n1.Вводите текст заглавными буквами и без пробелов, \nчтобы минимизировать шансы дешифровки\n\n2.Длина ключа должна быть равна длине сообщения  ", bg="black", foreground="red")
lbl3.place(x=20, y=290)



window.geometry('350x500')
window.mainloop()