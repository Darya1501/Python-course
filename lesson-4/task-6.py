from math import *

num = int(input('¬ведите целое четырехзначное число: '))
first_digit = num // 1000
second_digit = (num % 1000) // 100
thrid_digit = (num % 100) // 10
fourth_digit = num % 10

print(max(first_digit, second_digit, thrid_digit, fourth_digit))
