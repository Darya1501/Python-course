import random

def ask_question(question, sets):
    global enabled_chars
    print('Если в пароле нужны', question, 'введите Да: ')
    answer = input().lower()
    if answer.strip() == 'да':
        enabled_chars += sets

def generate_password(length, chars):
    password = ' '
    if length > 0:
        for i in range(length):
            random_index = random.randint(0, len(chars)-1)
            password += chars[random_index]  
        return password

print('\nПривет. Я - генератор паролей. \nЯ задам несколько уточняющих вопросов,на основе которых сгенерирую пароль. \nДавай начнем!', end='\n\n')

while True :
    print('Сколько паролей вы хотите сгенерировать? Введите число: ')
    count = input()
    
    if count.isdigit() and int(count) > 0:
        count = int(count)
    else:
        print('Неверный ввод, будет сгенерирован 1 пароль')
        count = 1
    
    print('Введите длину паролей:')
    length = input()
    
    if length.isdigit() and int(length) > 0:
        length = int(length)
    else:
        print('Неверное значение длины, будут сгенерировны пароли длиной 7 символов')
        length = 7
    
    enabled_chars = '0'
    digits = '1234567890'
    latin_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    latin_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian_lowercase_letters = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    russian_uppercase_letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!#$%&*+-=?@^_'

    ask_question('цифры,', digits)
    ask_question('строчные латинские буквы,', latin_lowercase_letters)
    ask_question('заглавные латинские буквы,', latin_uppercase_letters)
    ask_question('строчные русские буквы,', russian_lowercase_letters)
    ask_question('заглавные русские буквы,', russian_uppercase_letters)
    ask_question('знаки пунктуации,', punctuation)

    
    for i in range(count):
        password = generate_password(length, enabled_chars)    
        print('Сгенерированный пароль:', password)
    
    again = input('Еще раз? Да / нет: ') .lower()
    
    if again == 'нет':
        break
    elif again == 'да':
        continue
    else:
        print('Неизвестное значение, игра прекращена')
        break
    
print('До новых встреч!')
