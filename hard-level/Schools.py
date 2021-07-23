import sqlite3

connection = sqlite3.connect('Base_of_schools.db')
counter_of_students = 0


def get_next_command():
    print('\nВозможные действия: ')
    print('1 - Получить информацию о всех школах')
    print('2 - Добавить новую школу')
    print('3 - Получить полную информацию о школе')
    print('4 - Изменить информацию о школе')
    print('5 - Посмотреть учеников школы')
    print('6 - Добавить нового ученика школы')
    print('7 - Удалить имеющегося ученика школы')
    print('0 - Выйти из программы\n')

    while True:
        num = input('Что вы хотите сделать? Введите число от 0 до 7: ')
        if num.isdigit() and 0 <= int(num) <= 7:
            return int(num)
        else:
            print('Неверный ввод!')
            continue


class School:
    def __init__(self, number, name, address):
        self.number = number
        self.name = name
        self.address = address


class Student:
    def __init__(self, number, school, fio, age, class_num):
        self.school = school
        self.number = number
        self.fio = fio
        self.age = age
        self.class_num = class_num


class SchoolStorage:
    def __init__(self, connection):
        self.connection = connection
        cursor = connection.cursor()

        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE  type='table' AND name='schools' ''')

        if cursor.fetchone()[0] == 0:
            cursor.execute(''' CREATE TABLE schools(
            Number INTEGER PRIMARY KEY,
            Name TEXT,
            Address TEXT); ''')
            connection.commit()

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute('SELECT * FROM schools;')
        all_results = cursor.fetchall()
        schools = []

        for result in all_results:
            school = School(result[0], result[1], result[2])
            schools.append(school)

        return schools

    def safe(self, schools):
        for school in schools:
            self.add(school)

    def add(self, school):
        query = f''' INSERT INTO schools(Number,Name,Address) VALUES('{school.number}', '{school.name}', '{school.address}'); '''

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def remove(self, index):
        schools = self.get_all()
        school_for_delete = schools.pop(index)

        query = f''' DELETE FROM schools WHERE Number = '{school_for_delete.number}'; '''

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        
    def clear(self, schools):
        for _ in range(len(schools)):
            self.remove(0)
        
    def update(self, new_school):
        schools = self.get_all()
        for school in schools:
            if school.number == new_school.number:
                index = schools.index(school)
                self.clear(schools)
                schools[index] = new_school
                break
        
        self.safe(schools)
        

class StudentsStorage:
    def __init__(self, connection):
        self.connection = connection
        cursor = connection.cursor()

        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE  type='table' AND name='students' ''')

        if cursor.fetchone()[0] == 0:
            cursor.execute(''' CREATE TABLE students(
            Number INTEGER PRIMARY KEY,
            School_num INTEGER,
            FIO TEXT,
            Age INTEGER,
            Class_num INTEGER); ''')
            connection.commit()

    def get_all(self):
        global counter_of_students
        cursor = self.connection.cursor()

        cursor.execute('SELECT * FROM students;')
        all_results = cursor.fetchall()
        students = []

        for result in all_results:
            student = Student(result[0], result[1], result[2], result[3], result[4])
            students.append(student)
            counter_of_students = result[0]

        return students

    def safe(self, students):
        for student in students:
            self.add(students)

    def add(self, student):
        query = f''' INSERT INTO students(Number,School_num,FIO,Age,Class_num) VALUES('{student.number}', '{student.school}', '{student.fio}', '{student.age}', '{student.class_num}'); '''

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def remove(self, index):
        students = self.get_all()
        student_for_delete = students.pop(index)

        query = f''' DELETE FROM students WHERE Number = '{student_for_delete.number}'; '''

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


schoolStorage = SchoolStorage(connection)
studentsStorage = StudentsStorage(connection)

def is_school_in_base(number):
    schools = schoolStorage.get_all()
    result = [False, 0]
    for school in schools:
        if school.number == number:
            result = [True, school]
    return result
    
def print_all_schools():
    schools = schoolStorage.get_all()
    print('Все школы в базе данных: ')
    for school in schools:
        print(f'Школа № {school.number} - {school.name} - {school.address}')


def add_new_school():
    number = input('Введите номер школы: ')
    while not number.isdigit() or int(number) < 0:
        print('Некорректный ввод, номер школы - положительное целое число')
        number = input('Введите номер школы: ')
    number = int(number)
    
    while is_school_in_base(number)[0]:
        print('Школа с таким номером уже существует')
        number = input('Введите номер школы: ')
    
    name = input('Введите название школы: ')
    while len(name) < 3:
        print('Некорректный ввод, длина названия должна быть не меньше 3х символов')
        name = input('Введите название школы: ')
       
    address = input('Введите адресс школы: ')
    
    school = School(number, name, address)
    
    schoolStorage.add(school)

    
def print_school():
    while True:
        num = input('Информацию о какой школе вы хотите видеть? Введите номер: ')
        if not num.isdigit() or int(num) < 0:
            print('Некорректный ввод, номер школы - положительное целое число')
            continue
        num = int(num)
        
        res = is_school_in_base(num)
        if res[0]:
            print(f'Школа № {res[1].number} - {res[1].name} - {res[1].address}')
            break
        else:
            print('В базе нет школы с таким номером')
            continue

        

def change_school():
    while True:
        num = input('Информацию о какой школе вы хотите изменить? Введите номер: ')
        if not num.isdigit() or int(num) < 0:
            print('Некорректный ввод, номер школы - положительное целое число')
            continue
        num = int(num)
            
        res = is_school_in_base(num)
        if res[0]:
            name = res[1].name
            address = res[1].address 
            print(f'Школа № {res[1].number} - {name} - {address}')
            num = input('Что вы хотите изменить? Название школы - 1, адрес школы - 2, название и адрес - 3: ')
            
            while not num.isdigit() or int(num) < 1 or int(num) > 3:
                num = input('Некорректный ввод, повторите: ')
            num = int(num)
            
            if num == 1 or num == 3: 
                name = input('Введите название школы: ')
                while len(name) < 3:
                    print('Некорректный ввод, длина названия должна быть не меньше 3х символов')
                    name = input('Введите название школы: ')
            if num == 2 or num == 3:
                address = input('Введите адресс школы: ')
                
            school = res[1]
            school.name = name
            school.address = address
            schoolStorage.update(school)
            
            break
        else:
            print('В базе нет школы с таким номером')
            continue


def print_students():
    while True:
        num = input('Список учеников какой школы вы хотите посмотреть? Введите номер: ')
        if not num.isdigit() or int(num) < 0:
            print('Некорректный ввод, номер школы - положительное целое число')
            continue
        num = int(num)
        break
    
    print(f'{"Номер ученика":15} {"Имя ученика":30} {"Возраст":10} {"Класс":5}')
    students = studentsStorage.get_all()
    for student in students:
        if student.school == num:
            print(f'{str(student.number):15} {student.fio:30} {str(student.age):10} {str(student.class_num):5}')


def add_new_student():
    students = studentsStorage.get_all()
    global counter_of_students
    counter_of_students += 1
    
    while True:
        number = input('В какую школу вы хотите добавить ученика? Введите номер школы: ')
        while not number.isdigit() or int(number) < 0:
            print('Некорректный ввод, номер школы - положительное целое число')
            number = input('Введите номер школы: ')
        number = int(number)
        
        res = is_school_in_base(number)
        if res[0]:
            name = input('Введите полное имя ученика: ')
            fio = name.split()
            while len(fio) != 3 or len(name) < 8:
                print('Полное имя ученика - 3 слова не короче 2х букв')
                name = input('Введите полное имя ученика: ')
                fio = name.split()
            
            age = input('Введите возраст ученика: ')
            while not age.isdigit() or int(age) < 6 or int(age) > 18:
                print('Некорректный ввод, возраст ученика - положительное целое число от 6 до 18')
                age = input('Введите возраст ученика: ')
            age = int(age)
            
            class_num = input('Введите номер класса ученика: ')
            while not class_num.isdigit() or int(class_num) < 1 or int(class_num) > 11:
                print('Некорректный ввод, номер класса ученика - положительное целое число от 1 до 11')
                class_num = input('Введите номер класса ученика: ')
            class_num = int(class_num)
            
            student = Student(counter_of_students, number, name, age, class_num)
            studentsStorage.add(student)
            
            break
        
        else:
            print('В базе нет школы с таким номером')
            continue
    

def delete_student():
    print(f'{"Номер ученика":15} {"Имя ученика":30} {"Возраст":10} {"Класс":5}')
    students = studentsStorage.get_all()
    for student in students:
        print(f'{str(student.number):15} {student.fio:30} {str(student.age):10} {str(student.class_num):5}')
    
    while True:
        flag = False
        num = input('Введите номер ученика, которого вы хотите удалить: ')
        while not num.isdigit() or int(num) < 0 or int(num) > len(students):
            num = input('Некорректный ввод, повторите: ')
        num = int(num)
        
        for student in students:
            if student.number == num:
                studentsStorage.remove(students.index(student))
                flag = True
                break
        
        if flag: 
            break
        else:
            print('Такого ученика в базе нет')
            continue
    


print('Добро пожаловать в редактор школ')

while True:
    num = get_next_command()

    if num == 0:
        print('До новых встреч!')
        break
    elif num == 1:
        print_all_schools()
    elif num == 2:
        add_new_school()
    elif num == 3:
        print_school()
    elif num == 4:
        change_school()
    elif num == 5:
        print_students()
    elif num == 6:
        add_new_student()
    elif num == 7:
        delete_student()

    input('Для продолжения работы нажмите enter')