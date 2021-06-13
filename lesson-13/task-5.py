import random

count_of_attempts = 0

print('Добро пожаловать в игру "Загадай число"')
print('Загадайте число от 1 до 100')

secret_number = random.randint(1, 100)

mid = 50
left = 0
right = 100


while True:
    count_of_attempts += 1

    print('Ваше число равно, больше или меньше, чем ', mid, '?', sep='')
    answer = input()
    answer = answer.lower()

    if answer == 'больше' and left:
        left = mid
        mid = int(left + (right - left) / 2)
    elif answer == 'меньше':
        right = mid
        mid = int(left + (right - left) / 2)
    elif answer == 'равно':
        print('УРА! Компьютер угалал число за', count_of_attempts, 'попыток')
        break
    else:
        print('Я вас не понял, повторите, пожалуйста')
        continue

print('Спасибо за игру. Ждем вас ещё!')
