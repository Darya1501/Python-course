import random
from math import *

count_of_attempts = 0

print('Добро пожаловать в игру "Угадай число"')


def count_of_numbers():
    right_border = input('Из какого количества чисел будем угадывать? ')
    if right_border.isdigit():
        return int(right_border)
    else:
        print('Я вас не понял, установлено число 100')
        return 100


def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if 1 <= user_number <= right_border:
            return True
        else:
            return False
    else:
        return False


right_border = count_of_numbers()
secret_number = random.randint(1, right_border)


while True:
    print('Введите число от 1 до', right_border)
    user_number = input()
    count_of_attempts += 1

    if not is_valid(user_number):
        continue

    user_number = int(user_number)

    if secret_number > user_number:
        print('Загаданное число больше, чем введенное вами число')
    elif secret_number < user_number:
        print('Загаданное число меньше, чем введенное вами число')
    else:
        print('УРА! Вы угадали число за', count_of_attempts, 'попыток')
        print('Оптимальное число попыток для заданного количества чисел: ', ceil(log2(right_border)))
        play_again = input('Хотите сыграть ещё раз? Да/Нет ').lower()

        if play_again == 'нет':
            break
        elif play_again == 'да':
            count_of_attempts = 0
            right_border = count_of_numbers()
            secret_number = random.randint(1, right_border)
            continue
        else:
            print('Неизвестное значение, игра прекращена')
            break

print('Спасибо за игру. Ждем вас ещё!')
