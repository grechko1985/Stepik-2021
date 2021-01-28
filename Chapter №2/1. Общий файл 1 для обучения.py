# Для обучения теории
# Пример 1
a = 5
while a > 0:
    print(a, end=' ')
    a -= 1

# Пример 2
b = 5
while b <= 55:
    print(b)
    b += 2

# Пример 3
c = 5
while c <= 55:
    if c % 2 == 1:
        print(c)
    c += 1

# Пример 4
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        print(i)

# Пример 5
a = '*'
n = 0
while n < 6:
    n += 1
    print(n * a)

# Пример 6
k = int(input('Введите произвольное число: '))
d = 1
while d <= k:
    print('*' * d)
    d += 1

# Пример 7
stars = '*'
while stars < '**********':
    print(stars)
    stars += '*'

# Пример 8
l = int(input('Введите произвольное число: '))
stars = '*'
while len(stars) <= l:
    print(stars)
    stars += '*'


