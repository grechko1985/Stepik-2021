# Для обучения теории
# Пример 1 - вывести сумму всех нечетных чисел от a до b (включая обе границы)
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)

# Пример 2 - вывести сумму всех нечетных чисел от a до b (включая обе границы)(модифицированный)
a, b = input().split()
a = int(a)
b = int(b)
s = 0
if i % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
        s += i
print(s)

# Пример 3 - вывести сумму всех нечетных чисел от a до b (включая обе границы)(модифицированный)
a, b = (int(i) for i in input().split())
s = 0
if i % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
        s += i
print(s)