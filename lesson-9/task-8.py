# Сколко пятерок в последовательности от 1 до n

n = int(input())
count = 0

for i in range(1, n+1):
    j = i
    while j > 0:
        if j % 10  == 5:
            count += 1
        j = j // 10

print(count)