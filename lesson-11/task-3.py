# Верный ли ip-адрес?

ip = input('Введите ip-адрес: ')
parts = ip.split('.')
flag = 0

for part in parts:
    if int(part) < 0 or int(part) > 255:
        flag = -1

if flag == 0 and len(parts) == 4:
    print('YES')
else:
    print('NO')