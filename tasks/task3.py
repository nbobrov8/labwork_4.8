#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *

"""
напишите программу по описанию. Размеры многострочного текстового поля определяются значениями, 
введенными в однострочные текстовые поля. Изменение размера происходит при нажатии мышью на кнопку, 
а также при нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в фокусе, 
и белый, когда имеет фокус. Событие получения фокуса обозначается как <FocusIn> , потери – как <FocusOut>.
Для справки: фокус перемещается по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а
также при клике по ним мышью (к кнопкам последнее не относится).
"""


def button_click(event):
    txt1['width'] = ent1.get()
    txt1['height'] = ent2.get()


def focus_change(event, color):
    txt1['bg'] = color


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x300+300+300")
    root.title("Задание 3")

    f = Frame()
    f.pack()
    ent1 = Entry(f, width=3)
    ent2 = Entry(f, width=3)
    bt1 = Button(f, text='Изменить')
    txt1 = Text(width=25, height=25, bg='lightgrey')

    bt1.bind('<Button-1>', button_click)
    ent1.bind('<Return>', button_click)
    ent2.bind('<Return>', button_click)
    bt1.bind('<Return>', button_click)
    root.bind('<Return>', button_click)
    txt1.bind('<Return>', button_click)
    txt1.bind('<FocusIn>', lambda e, c="white": focus_change(e, c))
    txt1.bind('<FocusOut>', lambda e, c="lightgrey": focus_change(e, c))

    ent1.pack(side=LEFT)
    bt1.pack(side=RIGHT)
    ent2.pack(side=LEFT)
    txt1.pack()

    root.mainloop()
