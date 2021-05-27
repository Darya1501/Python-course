# Сколько в числе пятерок

a = int(input())
count = 0

while a != 0:
    if a % 10 == 5:
        count += 1
    a = a // 10
print(count)