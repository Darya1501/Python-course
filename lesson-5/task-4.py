# Вес дыни

weight = int(input('Введите вес дыни - целое число от 0 до 100: '))
if 0 <= weight <= 100:
    if weight > 2 and weight % 2 == 0:
        print('YES')
    else:
        print('NO')
else: 
    print('Дыня не может весить ', weight, 'кг', sep = '')
