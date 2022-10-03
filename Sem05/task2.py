# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

difficulty = input("Введите 1 если хотите играть против умного бота, иначе просто Enter: ")

candies = 110
first_player = randint(0, 1)
print(f"На столе лежит {candies} конфет.")
print("По результатам рандома первым ходит" + ["е Вы", " компьютер"][first_player] + "\n")


if first_player == 1:
    taken = candies % (28 + 1) \
        if difficulty == '1' \
        else randint(1, 28)
    candies -= taken
    print(f"Компьютер забрал {taken} конфет, осталось {candies}")

while candies != 0:
    taken = int(input("Сколько вы возьмете конфет? "))
    while not (1 <= taken <= 28 and taken <= candies):
        taken = int(input("Невалидный ввод. Введите от 1 до 28, но не больше общего кол-ва: "))
    candies -= taken
    if candies == 0:
        print("Вы победили, браво!")
        exit()
    else:
        taken = (candies % (28 + 1) if candies > 28 else candies) \
            if difficulty == '1' \
            else randint(1, 28 if candies > 28 else candies)
        candies -= taken
        print(f"Компьютер забрал {taken} конфет, осталось {candies}")
else:
    print(f"Компьютер победил")
