file = open('results.txt', 'r')
results = file.readlines()

print(f'{"ИМЯ":10}{"БАЛЛЫ":10}{"ЗВАНИЕ":10}')
for i in range(len(results)):
    strings = results[i].split()
    print(f'{strings[0]:10}{strings[1]:10}{strings[2]:10}')