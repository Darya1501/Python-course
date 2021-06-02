# Введенный символ - заглавная буква русского алфавита?

symbol = input()

if ord('А') <= ord(symbol) <= ord('Я'):
    print('YES')
else:
    print('NO')