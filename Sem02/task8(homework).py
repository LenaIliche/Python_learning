# Реализуйте алгоритм перемешивания списка.

import random

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Было: ", mylist)

for i in range(len(mylist) - 1):
    rand_index = random.randint(0, len(mylist) - 1)
    mylist[i], mylist[rand_index] = mylist[rand_index], mylist[i]

print("Стало:", mylist)
