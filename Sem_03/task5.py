# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input())
if n == 0:
    print("Can't be zero")
    exit()

a = 0
b = 1
fib_pos = [1]

for _ in range(n - 1):
    fib_pos.append(a + b)
    a, b = b, a + b

fib_neg = [-fib_pos[i] if (i % 2 != 0) else fib_pos[i] for i in range(len(fib_pos))][::-1]

print(fib_neg + [0] + fib_pos)