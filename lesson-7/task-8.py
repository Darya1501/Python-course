# Минимальное и максимальное в последовательности

n = int(input())

if n < 2:
    print('Последовательность должна состоять минимум из 2 цифр')
else: 
    min = max = int(input())
    for i in range(n-1):
        a = int(input())
        if a < min:
            min = a
        if a > max:
            max = a
    print('Минимум равен', min)
    print('Максимум равен', max)