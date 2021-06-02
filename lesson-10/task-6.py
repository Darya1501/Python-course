# Вывод всех цифр из строки

string = input()

for c in string:
    if c.isdigit():
        print(c, end='')