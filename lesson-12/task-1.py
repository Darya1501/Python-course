# Произведение количества цифр в двух числах 

def count_of_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count
    
first_num = int(input())
second_num = int(input())

total = count_of_digits(first_num) * count_of_digits(second_num)

print(total)


# Вопрос: как быть, если одно из введенных чисел - 0?
# Можно ли в данной задаче использовать вот такой вот код: 
#   count = 1
#   while num // 10 != 0:
#       count += 1
#       num = num // 10
# Или же нужно использовать if, и считать количество цифр только если num != 0