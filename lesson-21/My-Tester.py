import random
import os

class FileSystem:
    def exist(self, path):
        return os.path.exists(path)
    
    def __init__(self, address):
        while not FileSystem.exist(self, address):
            print('Файла с адресом', address, 'не существует!')
            address = input('Введите новый адрес: ')
        self.address = address
    
    def read_file(self):
        file = open(self.address, 'r')
        content = file.read()
        file.close()
        return content
    
    def add_to_file(self, content):
        file = open(self.address, 'a')
        file.write(content)
        file.close()      
    
    def update_file(self, content):
        file = open(self.address, 'w')
        file.write(content)
        file.close()
        

results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
questions = []
count_of_questions = 0
result = 0


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionsStorage:
    def get_all_qestions():
        global count_of_questions
        file = FileSystem('questions.txt')
        strings = FileSystem.read_file(file).strip('\n').split('\n')
        questions = []
        
        for string in strings:
            values = string.split('#')
            questions.append(Question(values[0], values[1]))
        
        count_of_questions = len(questions)
        return questions
    
    def add_question():
        while True:
            text = input('Введите текст вопроса (не короче 20 символов, оканчивается знаком вопроса): ')
            if len(text) < 20 or text[-1] != '?':
                continue
            break
        while True:
            answer = input('Введите ответ на вопрос (целое число): ')
            if not answer.isdigit():
                continue
            break
        question = Question(text, answer)
        
        file = FileSystem('questions.txt')
        FileSystem.add_to_file(file, f'{question.text}#{question.answer}\n')
        
    def remove_question():
        file = FileSystem('questions.txt')
        data = FileSystem.read_file(file)
        
        while True:
            text = input('Введите текст того вопроса, который вы хотите удалить: ')
            if not text in data:
                print('Такого вопроса нет!')
                continue
            break
        
        data = data.split('\n')
        
        for d in data:
            if text in d:
                data.remove(d)
        
        file = FileSystem('questions.txt')
        FileSystem.update_file(file, '\n'.join(data))
    
class User:
    def __init__(self, name, count_right_answers=0, result='Неизвестно'):
        self.name = name
        self.count = count_right_answers
        self.result = result    

    def accept_right_answers(self):
        self.count += 1
        
    def set_result(self, result):
        self.result = result
    
    
class UsersResultStorage:
    def safe_user_result(user):
        file = FileSystem('results.txt')
        FileSystem.add_to_file(file, f'{user.name}#{user.count}#{user.result}\n')

    def get_all():
        file = FileSystem('results.txt')
        data = FileSystem.read_file(file).split('\n')
        data.pop()
        users = []
        
        for d in data:
            values = d.split('#')
            user = User(values[0], values[1], values[2])
            users.append(user)
            
        return users

        
def get_result(count_right_answers):
    if count_of_questions != 0:
        persents = count_right_answers * 100 // count_of_questions
        return results[persents // 20]
    else:
        return 0

def show_results():
    print(f'{"ИМЯ":15}{"БАЛЛЫ":10}{"ЗВАНИЕ":10}')

    users = UsersResultStorage.get_all()
    
    for user in users:
        print(f'{user.name:15}{user.count:10}{user.result:10}')
        
        
def get_user_answer():
    user_answer = input()
    while not user_answer.isdigit():
        print('Введите число!')
        user_answer = input()
    return int(user_answer)

def play():
    questions = QuestionsStorage.get_all_qestions()
    name = input('Введите ваше имя: ')
    user = User(name)

    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)

        print(i + 1, 'вопрос:', questions[random_index].text)

        user_answer = get_user_answer()

        right_answer = questions[random_index].answer

        questions.pop(random_index)

        if user_answer == right_answer:
            user.accept_right_answers()

    result = get_result(user.count)
    user.set_result(result)

    print('Правильных ответов:', user.count)
    print('Вы,', user.name, '-', user.result)

    UsersResultStorage.safe_user_result(user)


while True:
    play()

    play_again = input('Хотите посмотреть результаты предыдущих тестов? ').lower()
    if play_again == 'да':
        show_results()
        
    add_question = input('Хотите добавить вопрос? ').lower()
    if add_question == 'да':
        QuestionsStorage.add_question()
        
    remove_question = input('Хотите удалить какой-либо вопрос? ').lower()
    if remove_question == 'да':
        QuestionsStorage.remove_question()

    play_again = input('Хотите пройти тест ещё раз? ').lower()

    if play_again == 'да':
        questions = QuestionsStorage.create_questions()
        print('Запускаю!')
        continue

    elif play_again == 'нет':
        print('До новых встреч!')
        break

    else:
        print('Неизвестный ответ, тестирование преращено')
        break
