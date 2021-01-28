# Для обучения теории
# Пример №1
# Дана геномная последовательность. Вывести, сколько раз в ней встречается нуклеотид цитозин.
# Входные данные CACCTGGAC - выход 4, GATTACA - выход 1
genome = input('Введите формулу: ')
count = 0
for i in genome:
    if i == 'C':
        count += 1
print(count)

# Вариант №2
genome = input('Введите формулу: ')
print(genome.count('C'))
