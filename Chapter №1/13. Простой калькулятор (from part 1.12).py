# Простой калькулятор
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