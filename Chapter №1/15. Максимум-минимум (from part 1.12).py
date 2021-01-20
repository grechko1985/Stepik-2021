# Максимум-минимум
print('Задача по сортировке чисел - мой вариант №1.')
a, b, c = int(input('Введите число a: ')), int(input('Введите число b: ')), int(input('Введите число c: '))
if b <= a <= c:
    print(c)
    print(b)
    print(a)
elif c <= a <= b:
    print(b)
    print(c)
    print(a)
elif a <= c <= b:
    print(b)
    print(a)
    print(c)
elif b <= c <= a:
    print(a)
    print(b)
    print(c)
elif c <= b <= a:
    print(a)
    print(c)
    print(b)
elif a <= b <= c:
    print(c)
    print(a)
    print(b)
else:
    print('Что-то пошло не так!')

print('Задача по сортировке чисел в сокращенном виде - мой вариант №2.')
a, b, c = int(input('Введите число a: ')), int(input('Введите число b: ')), int(input('Введите число c: '))
if b <= a <= c:
    print(str(c) + '\n' + str(b) + '\n' + str(a))
elif c <= a <= b:
    print(str(b) + '\n' + str(c) + '\n' + str(a))
elif a <= c <= b:
    print(str(b) + '\n' + str(a) + '\n' + str(c))
elif b <= c <= a:
    print(str(a) + '\n' + str(b) + '\n' + str(c))
elif c <= b <= a:
    print(str(a) + '\n' + str(c) + '\n' + str(b))
elif a <= b <= c:
    print(str(c) + '\n' + str(a) + '\n' + str(b))
else:
    print('Что-то пошло не так!')
