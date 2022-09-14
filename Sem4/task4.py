# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите k: "))

res = ""

# пишем строку до x^1 и без "= 0"
for i in range(k):
    num = randint(0, 100)
    if num == 0:
        continue
    elif num == 1:
        res += f" + x^{k - i}"
    else:
        res += f" + {num}x^{k - i}"

# обрезаем " + " в начале, а также "^1" в конце, если он есть
if len(res) != 0:
    if res[-1] == '1':
        res = res[3:-2]
    else:
        res = res[3:]
else:
    res = '0'

# дописываем x^0 и "= 0"
num = randint(0, 100)
if num != 0:
    res += f" + {num} = 0"
else:
    res += " = 0"

file_name = 'task4_result.txt'
f = open(file_name, 'w')
f.write(res)
f.close()
print(f"Результат записан в {file_name}")