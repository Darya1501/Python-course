import random

questions = ['Сколько будет два плюс два умноженное на два?', 'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 'На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 'Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 'Пять свечей горело, две потухли. Сколько свечей осталось?']
answers = [6, 9, 25, 60, 2]
results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']


def play():
    count_right_answers = 0    
    name = input('Введите ваше имя: ')
    
    for i in range(len(questions)):
        random_index = random.randint(0, len(questions)-1)
        
        print(i+1, 'вопрос:', questions[random_index])
        user_answer = input()
        
        if user_answer.isdigit():
            user_answer = int(user_answer)
        right_answer = answers[random_index]
        
        questions.pop(random_index)
        answers.pop(random_index)
        
        if user_answer == right_answer:
            count_right_answers += 1
        
    print('Правильных ответов:', count_right_answers)
    print('Вы,', name, '-', results[count_right_answers])


while True:
    play()
    
    play_again = input('Хотите пройти тест ещё раз? ').lower()
    
    if play_again == 'да':
        questions = ['Сколько будет два плюс два умноженное на два?', 'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 'На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 'Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 'Пять свечей горело, две потухли. Сколько свечей осталось?']
        answers = [6, 9, 25, 60, 2]        
        print('Запускаю!')
        continue
    
    elif play_again == 'нет':
        print('До новых встреч!')
        break
    
    else:
        print('Неизвестный ответ, тестирование преращено')
        break
