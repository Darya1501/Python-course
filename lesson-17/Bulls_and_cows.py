import random

def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    
    for i in range(4):
        random_index = random.randint(0, len(digits)-1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
        
    return secret_word


def calculate_bulls_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            counter += 1
    return counter


def calculate_cows_count(user_word, secret_word):
    counter = 0
    for i in range(len(user_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            counter += 1
    return counter


secret_word = generate_secret_word()
print('Найди число, задуманное компьютером')

while True:
    user_word = input('Твой вариант: ')
    
    if len(user_word) != 4 or not user_word.isdigit():
        print('Неверный ввод')
        continue
    
    flag = False
    for i in range(4):
        if user_word.count(user_word[i]) > 1:
            flag = True
            break
    if flag:
        print('Все числа должны быть разными!')
        continue
    
    bulls_count = calculate_bulls_count(user_word, secret_word)
    cows_count = calculate_cows_count(user_word, secret_word)
    
    print('Быков:', bulls_count, 'Коров:' , cows_count)
    
    if bulls_count == 4:
        print('Ура ты победил!')
        
        play_again = input('Играем ещё раз? Да/Нет ').lower()
        
        if play_again == 'нет':
            print('Отличная была игра!')
            break
        elif play_again == 'да':
            secret_word = generate_secret_word()
            print('Найди число, задуманное компьютером')
            continue
        else:
            print('Неизвестное значение, игра прекращена')
            break    
        
    