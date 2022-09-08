# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

half = ceil(len(mylist) / 2)
result = [mylist[i] * mylist[-i - 1] for i in range(half)]

print(result)
