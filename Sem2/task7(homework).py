# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input('Введите n: '))
mylist = [i for i in range(-n, n + 1)]
# print("Сгенерированный список: ", mylist)

print('Введите нужные индексы через пробел: ', end='')
indexes = [int(i) for i in input().split()]

prod = 1
for i in indexes:
    prod *= mylist[i]

print(prod)
