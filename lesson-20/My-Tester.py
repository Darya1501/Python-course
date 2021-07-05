import random

results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
questions = []
count_of_questions = 0
result = 0


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionsStorage:
    def create_questions():
        global count_of_questions
        questions = [Question('Сколько будет два плюс два умноженное на два?', 6),
                     Question('Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 9),
                     Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                     Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
                     Question('Пять свечей горело, две потухли. Сколько свечей осталось?', 2),
                     Question('Сколько граней у шестигранного карандаша?', 6),
                     Question('Сколько раз из чертовой дюжины можно вычесть число три?', 1),
                     Question('У фермера было 17 овец, и все, кроме девяти, сбежали. Сколько овец осталось у фермера?', 9)
                     ]
        count_of_questions = len(questions)
        return questions
    
class User:
    def __init__(self, name, result):
        self.name = name
        self.result = result    

class UsersResultStorage:
    def show_results():
        file = FileSystem('results.txt')
        data = FileSystem.read_file(file)
        lines = data.split('\n')
        lines.pop()
    
        print(f'{"ИМЯ":15}{"БАЛЛЫ":10}{"ЗВАНИЕ":10}')

        for line in lines:
            strings = line.split('#')
            print(f'{strings[0]:15}{strings[1]:10}{strings[2]:10}')
        
    def safe_user_result(user, count):
        file = FileSystem('results.txt')
        FileSystem.add_to_file(file, f'{user.name}#{count}#{user.result}\n')

        
class FileSystem:
    def __init__(self, address):
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
        
def get_result(count_right_answers):
    if count_of_questions != 0:
        persents = count_right_answers * 100 // count_of_questions
        return results[persents // 20]
    else:
        return 0

def get_user_answer():
    user_answer = input()
    while not user_answer.isdigit():
        print('Введите число!')
        user_answer = input()
    return int(user_answer)

def play():
    questions = QuestionsStorage.create_questions()
    count_right_answers = 0
    name = input('Введите ваше имя: ')

    for i in range(len(questions)):
        random_index = random.randint(0, len(questions) - 1)

        print(i + 1, 'вопрос:', questions[random_index].text)

        user_answer = get_user_answer()

        right_answer = questions[random_index].answer

        questions.pop(random_index)

        if user_answer == right_answer:
            count_right_answers += 1

    result = get_result(count_right_answers)
    
    user = User(name, result)

    print('Правильных ответов:', count_right_answers)
    print('Вы,', user.name, '-', user.result)

    UsersResultStorage.safe_user_result(user, count_right_answers)


while True:
    play()

    play_again = input('Хотите посмотреть результаты предыдущих тестов? ').lower()

    if play_again == 'да':
        UsersResultStorage.show_results()

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
