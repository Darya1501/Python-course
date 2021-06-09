# Произведение двух максимальных элементов в списках

def max_element(string):
    numbers = string.split()
    max = int(numbers[1])
    for number in numbers:
        if int(number) > max:
            max = int(number)
    return max
    
first_str = input()
second_str = input()

total = max_element(first_str) * max_element(second_str)

print(total)