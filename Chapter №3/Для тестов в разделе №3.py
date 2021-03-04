# Блок №1 - Открываем файл на чтение
with open('File1_for_3_9.txt') as inf:
    our_string = inf.readline().strip()     # удаляем все ненужные символы, перенос строки, пробелы вначале и т.д.
# Блок №2 - Считываение строки и перебор элементов, чтобы получить выходную строку
numbers = []                                # создаем пустой список для записи в него чисел з строки
letters = []                                # создаем пустой список для записи в него букв з строки
i = 0                                       # задаем индексу нолевое значение, для считывания строки по индексу
mod_string = our_string + 'b'               # добавляем в нашу строку + 1 элемент, чтобы не выйти за рамки при [i + 1]
while i in range(len(mod_string) - 1):      # считываем индексы от 0 до длины списка минус 1 лишний (добавленный нами)
    if mod_string[i] > 'A':                 # если элемент по индексу > 'A', тогда это буква.
        letters.append(mod_string[i])       # добавляем элемент в список букв
        i += 1                              # увеличиваем индекс на 1 для считывания следующего элемента
    elif mod_string[i] < 'A' and mod_string[i + 1] > 'A':   # иначе, если элемент < 'A' и след. элемент по индексу > 'A'
        numbers.append(mod_string[i])       # добавляем элемент в список цифр
        i += 1                              # увеличиваем индекс на 1 для считывания следующего элемента
    else:                                   # в противном случае, когда следуют две цифры
        numbers.append(mod_string[i] + mod_string[i + 1])   # склеиваем соседние цифры и добавляем элемент в список цифр
        i += 2                              # увеличиваем индекс на 2, чтобы пропустить сл. элемент, т.к. склеили
# Блок №3 - Формируем выходную строку на базе созданных списков
out_str = ''                                # создаем ПУСТУЮ выходную строку
for i in range(0, len(numbers)):            # задаем цикл для считывания элементов списка ЦИФР
    out_str = out_str + letters[i] * int(numbers[i])    # перемножаем  строку на число с каждой итерацией цикла
# Блок №4 - Выводим результат в файл
with open('File2_for_3_9.txt', 'w') as out:
    out.write(out_str)





s2 = []
with open('File1_for_3_9.txt') as inf:
    our_string = inf.readline().strip()  # удаляем ненужные символы,перенос строки,пробелы вначале и т.д.
    print(our_string)
# здесь файл уже закрыт
numbers = []
letters = []
mod_string = our_string + 'b'
i = 0
while i in range(len(mod_string) - 1):
    if mod_string[i] > 'A':
        letters.append(mod_string[i])
        i += 1
    elif mod_string[i] < 'A' and mod_string[i + 1] > 'A':
        numbers.append(mod_string[i])
        i += 1
    else:
        numbers.append(mod_string[i] + mod_string[i + 1])
        i += 2
out_str = ''
for i in range(0, len(numbers)):
    out_str = out_str + letters[i] * int(numbers[i])
with open('File2_for_3_9.txt', 'w') as out:
    out.write(out_str)
# здесь файл уже закрыт