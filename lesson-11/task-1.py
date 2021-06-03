# Моделирование поисковой системы

count = int(input('Введите количество слов в "архиве": '))
words = [0]*count

for i in range(count):
    words[i] = input(f'Введите {i+1}-е слово: ')
    
vocabulary = '*'.join(words)
vocabulary = vocabulary.lower()

word = input('Введите поисковый запрос: ')
word = word.lower()

position = vocabulary.find(word)
index = vocabulary.count('*', 0, position)

if position != -1:
    print('Ваш запрос встречается в слове', words[index])
else:
    print('Данного слова нет среди введенных ранее')
