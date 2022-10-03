# Вычислить число c заданной точностью d
# Пример: 
# при $d = 0.001, π = 3.141

from math import pi

d = float(input("Задайте точность: "))
d = len(str(d))

print(str(pi)[:d])
