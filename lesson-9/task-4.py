# Числа от 1 до n без 2-8, 128-256, 1024-2048 

n = int(input())

for i in range(1, n+1):
    if 2 <= i <= 8:
        continue
    elif 128 <= i <= 256:
        continue
    elif 1024 <= i <= 2048:
        continue
    else:
        print(i)