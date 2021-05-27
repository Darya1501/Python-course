# Сумма чисел, оканчивающихся на 1, 3, 7

n = int(input())
total = 0

for i in range(1, n+1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        total += i
print(total)