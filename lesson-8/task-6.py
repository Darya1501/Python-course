# Среднее арифметическое последовательности

a = int(input())
count = 0
total = 0

while a != 0:
    total += a
    count += 1
    a = int(input())
if count != 0:
    print(total / count)
else:
    print(0)