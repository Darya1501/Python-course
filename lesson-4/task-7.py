num = int(input('������� �����: '))
digit_1 = num % 10
digit_2 = num % 100 // 10
digit_3 = num % 1000 // 100

print('� �����', num, '����� ��������� ���� ���� �����', digit_1 + digit_2 + digit_3)
