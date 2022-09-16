from random import randint
from tkinter import *
from tkinter import messagebox

matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
victory_path = [[1, 1, 1], [2, 2, 2]]


def play(window, marker):
    def computer_moves():
        i = randint(0, 8)
        while matrix[i] != 0:
            i = randint(0, 8)
        matrix[i] = 2
        list_of_buttons[i].config(text='O', state=DISABLED)

    def process(i):
        matrix[i] = 1
        list_of_buttons[i].config(text='X', state=DISABLED)
        if not check_winner():
            computer_moves()
            check_winner()

    def a11():
        process(0)

    def a12():
        process(1)

    def a13():
        process(2)

    def a21():
        process(3)

    def a22():
        process(4)

    def a23():
        process(5)

    def a31():
        process(6)

    def a32():
        process(7)

    def a33():
        process(8)

    def draw_buttons_return_their_list(window):
        upper_left = Button(window, text="", height=2, width=4, command=a11)
        upper_cent = Button(window, text="", height=2, width=4, command=a12)
        upper_right = Button(window, text="", height=2, width=4, command=a13)
        cent_left = Button(window, text="", height=2, width=4, command=a21)
        cent_cent = Button(window, text="", height=2, width=4, command=a22)
        cent_right = Button(window, text="", height=2, width=4, command=a23)
        bott_left = Button(window, text="", height=2, width=4, command=a31)
        bott_cent = Button(window, text="", height=2, width=4, command=a32)
        bott_right = Button(window, text="", height=2, width=4, command=a33)
        list_of_buttons = [upper_left, upper_cent, upper_right, cent_left, cent_cent, cent_right, bott_left, bott_cent,
                           bott_right]
        for i in range(9):
            list_of_buttons[i].grid(row=i // 3 + 1, column=i % 3 + 1)
        if marker == "Компьютер":
            matrix[4] = 2
            list_of_buttons[4].config(text='O', state=DISABLED)
        return list_of_buttons

    list_of_buttons = draw_buttons_return_their_list(window)

    def reset():
        for i in range(9):
            matrix[i] = 0
            list_of_buttons[i].config(text='', state=NORMAL)
        if marker == "Компьютер":
            matrix[4] = 2
            list_of_buttons[4].config(text='O', state=DISABLED)

    def check_winner():
        if 0 not in matrix or \
                matrix[0:3] in victory_path or \
                matrix[3:6] in victory_path or \
                matrix[6:9] in victory_path or \
                matrix[0::3] in victory_path or \
                matrix[1::3] in victory_path or \
                matrix[2::3] in victory_path or \
                matrix[0::4] in victory_path or \
                matrix[2:-2:2] in victory_path:
            if messagebox.askyesno(message='Игра закончена :)\n\nЕще раз?'):
                reset()
            else:
                exit()
            return True
