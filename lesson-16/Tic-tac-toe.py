def create_field():
    field = []
    for i in range(3):
        field.append(['*']*3)
        
    return field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()
        
        
def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
        
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True
        
    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True    
    
    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True
    
    return False
        
    
def end_game(field):
    if win(field):
        return True
    
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
            
    return True

def input_of_coordinates(string):
    while True:
        print('Введите номер', string, end='')
        num = input()
        if num.isdigit() and 1 <= int(num) <= 3:
            num = int(num)
            return num
        else:
            print('Неверный ввод')
            continue

def play():
    field = create_field()
    current_symbol = 'X'
    while not end_game(field):
        print_field(field)
        
        while True:
            print('Ход игрока', current_symbol)
            row = input_of_coordinates('строки: ')
            column = input_of_coordinates('столбца: ')
            if field[row - 1][column - 1] == '*':
                field[row - 1][column - 1] = current_symbol
                break
            else:
                print('Данная клетка поля занята, выберите другую!')
                continue
        
        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'  
            
    print_field(field)
    if current_symbol == 'X':
        print('Ура! Победил О')
    else:
        print('Ура! Победил Х')
        

play()

while True:
    play_again = input('Хотите сыграть ещё раз? ').lower()
    if play_again == 'да':
        play()
        continue
    elif play_again == 'нет':
        print('До новых встреч!')
        break
    else:
        print('Не понял вас, игра преращена')
        break