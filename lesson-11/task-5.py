# Вывести уникальные элементы

string = input()
digits = string.split(' ')
count = 0

for digit in digits:
    if digits.count(digit) == 1:
        print(digit, end=' ')