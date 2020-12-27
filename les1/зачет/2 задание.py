from tkinter import *
import random
WIDTH = 800
HEIGHT = 600
raz_chasti_zmei = 20
game = True
def sosd_eda(): # Создаем еду для змейки
    global yabloko
    pos_x = raz_chasti_zmei * random.randint(1, (WIDTH - raz_chasti_zmei) / raz_chasti_zmei)
    pos_y = raz_chasti_zmei * random.randint(1, (HEIGHT - raz_chasti_zmei) / raz_chasti_zmei)
    yabloko = c.create_oval(pos_x, pos_y,
                          pos_x + raz_chasti_zmei, pos_y + raz_chasti_zmei,
                          fill="green")
class Ochki(object): # Подсчет очков
    def __init__(self):#отображения очков
        self.ochki = 0
        self.x = 55
        self.y = 15
        c.create_text(self.x, self.y, text="Счёт: {}".format(self.ochki), font="Arial 20",
                      fill="Yellow", tag="ochki", state='hidden')

    def schet(self): #счет очков
        c.delete("ochki")
        self.ochki += 1
        c.create_text(self.x, self.y, text="Счёт: {}".format(self.ochki), font="Arial 20",
                      fill="Yellow", tag="ochki")

    def reset(self):
        c.delete("ochki")
        self.ochki = 0


def main():
    global game
    if game:
        s.move()
        head_coords = c.coords(s.chast[-1].sluchai) #где голова
        x1, y1, x2, y2 = head_coords

        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:# столкновения с краями
            game = False

        elif head_coords == c.coords(yabloko):# Поедание яблока
            s.add_chast_zmei()
            c.delete(yabloko)
            sosd_eda()
        else:# Поедание змейки
            for index in range(len(s.chast) - 1):
                if head_coords == c.coords(s.chast[index].sluchai):
                    game = False
        root.after(140, main)
    else:
        set_state(restart_knop, 'normal')
        set_state(konec, 'normal')
        set_state(close_knop, 'normal')


class chast_zmei(object):
    def __init__(self, x, y):
        self.sluchai = c.create_rectangle(x, y,
                                           x + raz_chasti_zmei, y + raz_chasti_zmei,
                                           fill="green")


class Zmeyka(object):

    def __init__(self, chast):
        self.chast = chast

        # Варианты движения
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}

        #  направление движения
        self.vector = self.mapping["Right"]

    def move(self):
        for index in range(len(self.chast) - 1):
            golova = self.chast[index].sluchai
            x1, y1, x2, y2 = c.coords(self.chast[index + 1].sluchai)
            c.coords(golova, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.chast[-2].sluchai)
        c.coords(self.chast[-1].sluchai,
                 x1 + self.vector[0] * raz_chasti_zmei, y1 + self.vector[1] * raz_chasti_zmei,
                 x2 + self.vector[0] * raz_chasti_zmei, y2 + self.vector[1] * raz_chasti_zmei)

    def add_chast_zmei(self):#Добавляем часть змейки
        ochki.schet()
        last_seg = c.coords(self.chast[0].sluchai)
        x = last_seg[2] - raz_chasti_zmei
        y = last_seg[3] - raz_chasti_zmei
        self.chast.insert(0, chast_zmei(x, y))

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
    def reset_snake(self):
        for golova in self.chast:
            c.delete(golova.sluchai)

def set_state(item, state):
    c.itemconfigure(item, state=state)
    c.itemconfigure(yabloko, state='hidden')
def clicked(event):
    global game
    s.reset_snake()
    game = True
    c.delete(yabloko)
    ochki.reset()
    c.itemconfigure(restart_knop, state='hidden')
    c.itemconfigure(konec, state='hidden')
    c.itemconfigure(close_knop, state='hidden')
    new_game()
def new_game():
    global s
    sosd_eda()
    s = new_zmeya()
    c.bind("<KeyPress>", s.change_direction) # Реагируем на нажатие клавиш
    main()
def new_zmeya():
    chast = [chast_zmei(raz_chasti_zmei, raz_chasti_zmei),
                chast_zmei(raz_chasti_zmei * 2, raz_chasti_zmei),
                chast_zmei(raz_chasti_zmei * 3, raz_chasti_zmei)]
    return Zmeyka(chast)
def close_win(root):
    exit()
root = Tk()
root.title("Змейка")
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
c.grid()
c.focus_set()
konec = c.create_text(WIDTH / 2, HEIGHT / 2, text="Ты проиграл!",
                               font='Arial 20', fill='red',
                               state='hidden')
restart_knop = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 3,
                             font='Arial 25',
                             fill='green',
                             text="Начать новую игру",
                             state='hidden')
close_knop = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 5, font='Arial 25',
                          fill='green',
                          text="Выход из игры",
                          state='hidden')
c.tag_bind(restart_knop, "<Button-1>", clicked)
c.tag_bind(close_knop, "<Button-1>", close_win)

ochki = Ochki()
new_game()

root.mainloop()