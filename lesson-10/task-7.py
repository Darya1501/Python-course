# Вывести введенное имя в формате Фамилия И.О.

surname = input()
name = input()
patronymic = input()

print(f'{surname} {name[0]}.{patronymic[0]}.')