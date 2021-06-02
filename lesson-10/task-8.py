# Количесво одинаковых идущих подряд символов

string = input()
count = 0

for i in range(len(string)):
    if string.count(string[i], i) > 1:
        count += 1

print(count)