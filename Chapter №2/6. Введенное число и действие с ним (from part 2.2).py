# Напишите программу, которая считывает целые числа с консоли по одному числу в строке. Для каждого введённого числа
# проверить- если число меньше 10, то пропускаем это число; если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
number = 0
while number <= 100:
    number = int(input('Введите ваше число: '))
    if number < 10:
        continue
    elif 10 <= number <= 100:
        print(number)

# Вариант №1 с сайта
while True:
    number = int(input())
    if number > 100:
        break
    if number < 10:
        continue
    print(number)

# Вариант №2 с сайта
while True:
    n = int(input())
    if n < 10:
        continue
    elif n > 100:
        break
    else:
        print(n)
