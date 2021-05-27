# Все числа в последовательности нечетные

n = int(input())
flag = 0

for i in range(n):
    a = int(input())
    if a % 2 == 1:
        flag += 1
if flag == n and n != 0:
    print('YES')
else:
    print('NO')