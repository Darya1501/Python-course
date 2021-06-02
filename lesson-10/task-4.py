# Изменение регистра латинских букв

symbol = input()
char = ord(symbol)

if ord('A') <= char <= ord('Z') or ord('a') <= char <= ord('z'):
    if symbol.islower():
        symbol = symbol.upper()
    else:
        symbol = symbol.lower()

print(symbol)