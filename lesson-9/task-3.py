# Есть ли в числе единица? 

num = int(input())
flag = 0

while num > 0:
    if num % 10 == 1:
        flag = 1
        break
    num = num // 10

if flag == 1:
    print('Yes')
else:
    print('No')