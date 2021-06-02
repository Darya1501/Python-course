# Вывод всех символов, которые находятся между введенными

sym1 = ord(input())
sym2 = ord(input())

if sym1 < sym2:
    for i in range(sym1, sym2 + 1):
        print(chr(i), end=' ')
else:
    for i in range(sym2, sym1 + 1):
        print(chr(i), end=' ')