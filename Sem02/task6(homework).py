# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

n = int(input())
mylist = [(1 + 1 / k) ** k for k in range(1, n + 1)]

print(sum(mylist))
