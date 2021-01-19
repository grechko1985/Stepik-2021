# Условия
# Найти наибольшее из двух чисел
a = 4
b = 7
if a >= b:
    print(a)
else:
    print(b)

# Вариант №2
a = 4
b = 7
m = a
if b >= m:
    m = b
print(m)

# Вывод результата деления одного числа на другое
c = int(input())
d = int(input())
if d != 0:
    print(c / d)
else:
    print('Деление невозможно')
    d = int(input('Введите ненулевое значение: '))
    if d == 0:
        print('Вы не справились!')
    else:
        print(c / d)

