# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
# и после первого введенного нуля выводит сумму полученных на вход чисел.
# Мой вариант
number = int(input('Введите ваше число: '))
sum_numbers = 0
while number != 0:
    sum_numbers += number
    number = int(input('Введите ваше число: '))
print(sum_numbers)
