num = int(input('Введите число: '))
digit_1 = num % 10
digit_2 = num % 100 // 10
digit_3 = num % 1000 // 100

print('У числа', num, 'сумма последних трех цифр равна', digit_1 + digit_2 + digit_3)
