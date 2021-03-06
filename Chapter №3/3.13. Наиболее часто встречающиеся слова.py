# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
# смотреть, как, например, на наиболее часто используемые. Напишите программу, которая считывает текст из файла
# (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз
# оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк)
# В качестве ответа укажите вывод программы, а не саму программу. Слова, написанные в разных регистрах, считаются
# одинаковыми.
our_text = ''                               # объявляем пустую строку для считывания в нее текста
d = {}                                      # объявляем словарь d, в который будем записывать слово и количество повтор.
with open('File1_for_3_13.txt') as text:    # открываем файл на чтение
    for word in text:                       # считываем посимвольно все символы текста
        our_text += word.lower()            # результат записываем в виде строки - ВСЕ символы в нижнем регистре
our_list = our_text.split()                 # преобразуем полученную строку our_text в список our_list
our_list.sort()                             # сортируем список
count = 1                                   # задаем счетчик для считывания количества повторений
for i in range(0, len(our_list) - 1):       # считываем все элементы списка по индексу в диапазоне от 0 до len(our_list)
    if our_list[i] == our_list[-len(our_list) + i + 1]:    # если текущий элемент списка равен следующему
        count += 1                                         # тогда увеличиваем счетчик на 1
    else:                                                  # иначе
        d[our_list[i]] = count                             # добавляем в словарь текущий элемент списка и значение повт.
        count = 1                                          # сбрасываем счетчик в 1
max_val = max(d.values())                                  # ищем максимальное значение в СЛОВАРЕ d
out_d = {k : v for k, v in d.items() if v == max_val}      # записываем мак. значение и его ключ в отдельный словарь
for key, value in out_d.items():                           # считываем словарь
    print(key, value)                                      # печатаем ключе и его значение в виде key value







