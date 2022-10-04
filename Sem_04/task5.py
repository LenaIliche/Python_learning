# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def parse_and_split(arg_list):
    res = []
    for elem in arg_list:
        if 'x^' in elem:
            res.append([int(i) if len(i) != 0 else 1 for i in elem.split('x^')])
        else:
            res.append([int(elem[:-1]) if len(elem[:-1]) != 0 else 1, int('x' in elem)])
    return res


f1 = open('task5_input1.txt', 'r')
f2 = open('task5_input2.txt', 'r')
first = f1.read().replace('+', '').replace('= 0', '').split()
second = f2.read().replace('+', '').replace('= 0', '').split()
f1.close()
f2.close()
print(first)
print(second)
print()

first = parse_and_split(first)
second = parse_and_split(second)
print(first)
print(second)

max_power = max(first[0][1], second[0][1])
res = []
for power in range(max_power, -1, -1):
    if first[0][1] == power:
        if second[0][1] == power:
            res.append([first[0][0] + second[0][0], power])
            second.pop(0)
        else:
            res.append([first[0][0], power])
        first.pop(0)
    elif second[0][1] == power:
        res.append([second[0][0], power])
        second.pop(0)
print()
print(res)

res_str = ""
for elem in res:
    res_str += str(elem[0])
    if elem[1] >= 2:
        res_str += "x^" + str(elem[1]) + " + "
    elif elem[1] == 1:
        res_str += "x + "
    elif elem[1] == 0:
        res_str += " + "
res_str = res_str[:-2] + '= 0'
print()
print(res_str)

f = open("task5_result.txt", 'w')
f.write(res_str)
f.close()
