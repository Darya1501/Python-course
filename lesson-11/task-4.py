# Количество одинаковых элементов

string = input()
digits = string.split(' ')
count = 0

for i in range(len(digits)):
    if digits.count(digits[i]) > 1:
        count += digits.count(digits[i]) - 1

count = int(count / 2)
print(count)
