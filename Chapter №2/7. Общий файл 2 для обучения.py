# Для обучения теории
# Пример 1
for i in 2, 3, 5:
    print(i * i)

# Пример 2
for i in range(10):
    print(i * i)

# Пример 3
# Вывести квадрат
n = int(input())
for i in range(n):
    print('*' * n)

# Пример 4
# Решение с вложенными циклами
n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
