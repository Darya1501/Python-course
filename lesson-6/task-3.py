# Статья, в которой больше всего символов

string_1 = input()
string_2 = input()
string_3 = input()

len_1 = len(string_1)
len_2 = len(string_2)
len_3 = len(string_3)

if max(len_1, len_2, len_3) == len_1:
    print(string_1)
elif max(len_1, len_2, len_3) == len_2:
    print(string_2)
else:
    print(string_3)