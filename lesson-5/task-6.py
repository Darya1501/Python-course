# Рулетка

a = int(input())
if a == 0:
    result = 'зеленый'
elif 0 < a <= 10:
    if a % 2 == 1:
        result = 'красный'
    else:
        result = 'черный'
elif 10 < a <= 18:
    if a % 2 == 1:
        result = 'черный'
    else:
        result = 'красный'
elif 18 < a <= 28:
    if a % 2 == 1:
        result = 'красный'
    else:
        result = 'черный'
elif 28 < a <= 36:
    if a % 2 == 1:
        result = 'черный'
    else:
        result = 'красный'
else:
    result = 'ошибка ввода'
print(result)
