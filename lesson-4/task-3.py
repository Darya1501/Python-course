num = int(input('������� ����������� �����: '))

first_digit = num // 100
second_digit = (num % 100) // 10
thrid_digit = num % 10

num_1 = first_digit + second_digit + thrid_digit
num_2 = first_digit * second_digit * thrid_digit
print(first_digit, second_digit, thrid_digit)
print('����� ���� �����', num, '�����', num_1)
print('������������ ���� �����', num, '�����', num_2)
