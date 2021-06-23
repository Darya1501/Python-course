questions = ['Сколько будет два плюс два умноженное на два?', 'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 'На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 'Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 'Пять свечей горело, две потухли. Сколько свечей осталось?']

answers = [6, 9, 25, 60, 2]

results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']

count_right_answers = 0

name = input('Введите ваше имя: ')

for i in range(len(questions)):
    
    print(i+1, 'вопрос:', questions[i])
    user_answer = int(input())
    
    right_answer = answers[i]
    
    if user_answer == right_answer:
        count_right_answers += 1
        
print('Правильных ответов:', count_right_answers)
print('Вы,', name, '-', results[count_right_answers])


# Решены задачи 2, 3, 4