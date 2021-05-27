# Замечательное число

a = int(input())
a_copy = a
total = 0

while a != 0:
    total += a % 10
    a = a // 10
if a_copy % total == 0:
    print('YES')
else:
    print('NO')