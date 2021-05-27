# Произведение количества положительных и отрицательных чисел

a = int(input())
count_positive = 0
count_negative = 0

while a != 0:
    if a < 0:
        count_negative += 1
    if a > 0:
        count_positive += 1
    a = int(input())

print(count_negative * count_positive)