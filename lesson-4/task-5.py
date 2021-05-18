count = int(input('Введите количество секунд: '))

seconds = count % 60
minutes = (count // 60) % 60
hours = count // 3600

print(count, 'секунд - это', hours, 'часа', minutes, 'минут', seconds, 'секунд')