import random
russian_letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word

def play(question, secret_word):
    count_of_attempts = 0
    secret_word = secret_word.upper()
    
    user_word = '*' * len(secret_word)
    
    print('\nВОПРОС:', question, '\nCЛОВО:', user_word)
    
    while user_word != secret_word:
        print('Введите букву:', end=' ')
        user_char = input().upper()
        count_of_attempts += 1
        
        if len(user_char) != 1:
            continue
        
        if not user_char in russian_letters:
            print('Нужна буква русского алфавита')
            continue
            
        if user_char in  user_word:
            print('Вы уже угадали эту букву!')
            count_of_attempts -= 1
            continue        
        
        new_user_word = update_user_word(secret_word, user_word, user_char)
        
        if user_word == new_user_word:
            print('К сожалению, такой буквы нет в слове')
        else:
            print('Поздравляем, такая буква есть в слове')
            
        user_word = new_user_word
        
        print(user_word)
        
    print('Ура, вы угадали загаданное слово', user_word, 'за', count_of_attempts, 'ходов!\n')
    
    
print('\nДобро пожаловать в игру "Поле Чудес"!')

while True:   
    questions = ['Древнейшие каменные здания возводились из обтёсанных каменных глыб, \nа это изобретение позволило зодчим древнего Рима возвести шедевры архитектуры, \nпоражавшие воображение и их современников и туристов наших дней.', 'Этот предмет изобрели в Древнем Египте. Тогда он полностью изготовлялся из дерева. \nПо идее египетских мастеров в 19 веке Линиус Йейл изготовил современную металлическую модель, \nсохранив полностью принцип действия. У нас он обычно называется “английским”.', 'В 14-16 веках его носили…мужчины. С 17 века его стали носить женщины. \nНазваний у него было много: шторник, клинник, пестряк, наколоточник и другие. \nДо наших дней дошло лишь одно название - какое?', 'Что раньше называли “костотрясом”, “пауком”, а теперь называют “быстрой ногой”?', 'Один из древнейших видов искусства – танец. Как звали музу танцев?']
    secret_words = ['Бетон', 'Замок', 'Сарафан', 'Велосипед', 'Терпсихора']
    
    random_index = random.randint(0, len(questions)-1)
    
    play(questions[random_index], secret_words[random_index])

    play_again = input('Хотите сыграть ещё раз? ').lower()
    if play_again == 'да':
        print('Понял вас, запускаю!')
        continue
    elif play_again == 'нет':
        print('До новых встреч!')
        break
    else:
        print('Не понял вас, игра преращена')
        break
