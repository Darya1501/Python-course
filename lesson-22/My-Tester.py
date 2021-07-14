import random
import os
import jsonpickle

jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)

results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
questions = []
users = []
count_of_questions = 0
result = 0


class FileSystem:
    def exist(path):
        return os.path.exists(path)

    def __init__(self, address):
        self.address = address

    def read_file(address):
        file = open(address, 'r')
        content = file.read()
        file.close()
        return content

    def add_to_file(address, content):
        file = open(address, 'a')
        file.write(content)
        file.close()

    def update_file(address, content):
        file = open(address, 'w')
        file.write(content)
        file.close()


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionsStorage:
    def __init__(self):
        self.file_name = 'questions.json'
    
    def get_all_qestions(self):        
        if not FileSystem.exist(self.file_name):
            questions = [Question('Сколько будет два плюс два умноженное на два?', 6),
                         Question('Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 9),
                         Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                         Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60)
                         ]
            self.safe_questions(questions)

        data = FileSystem.read_file(self.file_name)
        questions = jsonpickle.decode(data)
        return questions

    def safe_questions(self, questions):
        json_data = jsonpickle.encode(questions)
        FileSystem.update_file(self.file_name, json_data)
        
    def add_question(self, question):
        questions = self.get_all_qestions()
        questions.append(question)
        self.safe_questions(questions)
        

    def remove_question(self, question):
        questions = self.get_all_qestions()
        questions.pop(question)
        self.safe_questions(questions)        
       
questionsStorage = QuestionsStorage()
def add_new_question():
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
    questionsStorage.add_question(question)
    
def delete_question():
    
    old_questions = questionsStorage.get_all_qestions()
    
    for i in range(len(old_questions)):
        print(f'{i+1}. {old_questions[i].text}')
    
    while True:
        number = input('Введите номер того вопроса, который вы хотите удалить: ')
        if not number.isdigit() or int(number) < 1 or int(number) > len(old_questions):
            print('Такого вопроса нет!')
            continue
        break
    old_questions.pop(int(number)-1)
            
    questionsStorage.safe_questions(old_questions)

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
    def __init__(self):
        self.file_name = 'results.json'
        
    def safe_user_result(self, users):
        json_data = jsonpickle.encode(users)
        FileSystem.update_file(self.file_name, json_data)

    def get_all(self):
        if not FileSystem.exist(self.file_name):
            users = []
            self.safe_user_result(users)
        
        data = FileSystem.read_file(self.file_name)
        users = jsonpickle.decode(data)
        return users
    
    def add_user(self, user):
        users = self.get_all()
        users.append(user)
        self.safe_user_result(users)   
        
usersResultStorage = UsersResultStorage()

def get_result(count_right_answers, count_of_questions):
    if count_of_questions != 0:
        persents = count_right_answers * 100 // count_of_questions
        return results[persents // 20]
    else:
        return 0


def show_results():
    print(f'{"ИМЯ":15}{"БАЛЛЫ":10}{"ЗВАНИЕ":10}')

    users = usersResultStorage.get_all()

    for user in users:
        print(f'{user.name:15}{str(user.count):10}{user.result:10}')


def get_user_answer():
    user_answer = input()
    while not user_answer.isdigit():
        print('Введите число!')
        user_answer = input()
    return int(user_answer)


def play():
    questions = questionsStorage.get_all_qestions()
    count_of_questions = len(questions)
    name = input('Введите ваше имя: ')
    user = User(name)

    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)

        print(i + 1, 'вопрос:', questions[random_index].text)

        user_answer = get_user_answer()

        right_answer = questions[random_index].answer

        questions.pop(random_index)

        if user_answer == int(right_answer):
            user.accept_right_answers()

    result = get_result(user.count, count_of_questions)
    user.set_result(result)

    print('Правильных ответов:', user.count)
    print('Вы,', user.name, '-', user.result)

    usersResultStorage.add_user(user)


while True:
    play()

    play_again = input('Хотите посмотреть результаты предыдущих тестов? ').lower()
    if play_again == 'да':
        show_results()

    add_question = input('Хотите добавить вопрос? ').lower()
    if add_question == 'да':
        add_new_question()

    remove_question = input('Хотите удалить какой-либо вопрос? ').lower()
    if remove_question == 'да':
        delete_question()

    play_again = input('Хотите пройти тест ещё раз? ').lower()

    if play_again == 'да':
        questions = questionsStorage.get_all_qestions()
        print('Запускаю!')
        continue

    elif play_again == 'нет':
        print('До новых встреч!')
        break

    else:
        print('Неизвестный ответ, тестирование преращено')
        break
