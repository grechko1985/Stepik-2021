# Простой калькулятор
print('Мой вариант.')
num_1 = float(input())
num_2 = float(input())
operation = input()
if num_2 == 0 and (operation == '/' or operation == 'mod' or operation == 'div'):
    print('Деление на 0!')
elif operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '/':
    print(num_1 / num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == 'mod':
    print(num_1 % num_2)
elif operation == 'pow':
    print(num_1 ** num_2)
elif operation == 'div':
    print(num_1 // num_2)

# Вариант №1 с сайта
print('Вариант №1 с сайта')
a, b = float(input()), float(input())
do = input()
if do == '+':
    print(a + b)
elif do == '-':
    print(a - b)
elif do == '*':
    print(a * b)
elif do == 'pow':
    print(a ** b)
elif b == 0:
    print("Деление на 0!")
elif do == 'mod':
    print(a % b)
elif do == '/':
    print(a / b)
else:
    print(a // b)