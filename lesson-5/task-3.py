# Счастливый билет

num = int(input('Введите номер билета: '))

first_digit = num // 100000
second_digit = num % 100000 // 10000
third_digit = num % 10000 // 1000
fourth_digit = num % 1000 // 100
fifth_digit = num % 100 // 10
sixth_digit = num % 10

first_sum = first_digit + second_digit + third_digit
second_sum = fourth_digit + fifth_digit + sixth_digit

if first_sum == second_sum:
    print('Билет', num, 'счастливый')
else:
    print('Билет', num, 'НЕ счастливый')
