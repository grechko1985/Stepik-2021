# Оператор break - читаем 5 пар чисел и выводим их произведение
print('Программа №1')
i = 0
while i < 5:
    a, b = input('Введите пару чисел в формате "a b": ').split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break   # завершение цикла в случае ввода a = 0 и b = 0
    print(a*b)
    i += 1

# Оператор continue - читаем 5 пар чисел и выводим их произведение
print('\nПрограмма №2')
i = 0
while i < 5:
    a, b = input('Введите пару чисел в формате "a b": ').split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break   # завершение цикла в случае ввода a = 0 и b = 0
    if (a == 0) or (b == 0):
        continue   # переходим к слеующей итерации
    print(a*b)
    i += 1
