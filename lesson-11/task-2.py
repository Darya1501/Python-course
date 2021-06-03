# Разбиение адреса файла по частям

address = input('Введите адрес файла: ')
flouders = address.split('\\')

for flouder in flouders:
    print(flouder)