# Хотя бы одно нечетное в последовательности

n = int(input())
flag = 0

for i in range(n):
    a = int(input())
    if a % 2 == 1:
        flag = 1
if flag == 1:
    print('YES')
else:
    print('NO')