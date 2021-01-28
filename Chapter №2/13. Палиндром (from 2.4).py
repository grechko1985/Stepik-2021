# Задача - палиндром
# Дана геномная последовательность. Проверить, является ли она палиндромом (строкой, что читается одинаково в любом
# направлении).
# Входные данные CAGGTGGAC - результат Yes, GARRACA - результат NO.
# Мой вариант
s = input('Введите вашу строку: ')
if s[::-1] == s:
    print('YES')
else:
    print('NO')

# Вариант 1 с сайта
s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')

# Вариант 2 с сайта
s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
        break
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')