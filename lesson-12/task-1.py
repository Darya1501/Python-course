# Произведение количества цифр в двух числах 

def count_of_digits(num):
    count = 0
    
    if num == 0:
        return 1
        
    while num > 0:
        count += 1
        num = num // 10
    return count
    
first_num = int(input())
second_num = int(input())

total = count_of_digits(first_num) * count_of_digits(second_num)

print(total)
