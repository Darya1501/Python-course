# Замечательное число

a = int(input())
max = 0
min = a

while a != 0:
    num = a % 10
    if num > max:
        max = num
    if num < min:
        min = num
    a = a // 10

print('Максимальная цифра равена', max)
print('Минимальная цифра равена', min)