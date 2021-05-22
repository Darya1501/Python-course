# Проверка почты

mail = input()

if '@' in mail and '.' in mail:
    print('Корректный')
else:
    print('Некорректный')