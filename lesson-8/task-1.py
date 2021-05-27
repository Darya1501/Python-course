# Сколько раз число можно поделить на 2

a = int(input())
count = 0

while a % 2 == 0 and a != 0:
    a = a // 2
    count += 1
print(count)