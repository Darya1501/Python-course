count = int(input('������� ���������� ������: '))

seconds = count % 60
minutes = (count // 60) % 60
hours = count // 3600

print(count, '������ - ���', hours, '����', minutes, '�����', seconds, '������')