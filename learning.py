n = int(input())
print('1')

if n > 1:
    print('1')
    previous = 1
    current = 1
    for _ in range(n - 2):
        print(previous + current)
        previous, current = current, previous + current
