import random
from math import *

results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
questions = []
answers = []
count_of_questions = 0
result = 0

def create_questions():
    global questions, answers, count_of_questions
    questions = ['Сколько будет два плюс два умноженное на два?', 'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 'На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 'Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 'Пять свечей горело, две потухли. Сколько свечей осталось?', 'Сколько граней у шестигранного карандаша?', 'Сколько раз из чертовой дюжины можно вычесть число три?', 'У фермера было 17 овец, и все, кроме девяти, умерли. Сколько овец осталось у фермера?']
    answers = [6, 9, 25, 60, 2, 6, 1, 9]
    count_of_questions = len(questions)
    
def get_user_answer():
    user_answer = input()    
    while not user_answer.isdigit():
        print('Введите число!')
        user_answer = input()  
    return int(user_answer)

def get_result(count_right_answers):
    one_percent = count_of_questions / 100
    if one_percent != 0 and count_of_questions != 0:
        persents = count_right_answers / one_percent
        return ceil(6 * (persents / 100)) - 1
    else:
        return 0

def play():
    create_questions()
    count_right_answers = 0    
    name = input('Введите ваше имя: ')
    
    for i in range(len(questions)):
        random_index = random.randint(0, len(questions)-1)
        
        print(i+1, 'вопрос:', questions[random_index])
        
        user_answer = get_user_answer()
        
        right_answer = answers[random_index]
        
        questions.pop(random_index)
        answers.pop(random_index)
        
        if user_answer == right_answer:
            count_right_answers += 1
            
    
    print('Правильных ответов:', count_right_answers)
    print('Вы,', name, '-', results[get_result(count_right_answers)])
    
    file = open('results.txt', 'a')
    string = name + ' ' + str(count_right_answers) + ' ' + str(results[get_result(count_right_answers)]) + '\n'
    file.write(string)
    file.close()


while True:
    play()
    
    play_again = input('Хотите пройти тест ещё раз? ').lower()
    
    if play_again == 'да':
        create_questions()      
        print('Запускаю!')
        continue
    
    elif play_again == 'нет':
        print('До новых встреч!')
        break
    
    else:
        print('Неизвестный ответ, тестирование преращено')
        break