# Высокосный год
year = int(input('Введите год: '))
if 1900 <= year <= 3000:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Введенный вами год не соответвует требованиям!')
