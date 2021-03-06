# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно. Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с
# помощью кодирования повторов, и производит обратную операцию, получая исходный текст. Запишите полученный текст в
# файл и прикрепите его, как ответ на это задание. В исходном тексте не встречаются цифры, так что код однозначно
# интерпретируем. Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у
# вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными
# данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
# Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
with open('File1_for_3_9.txt', 'r') as f:           # читаем исходную строку из файла
    s = f.readline().strip()
i = 0                                               # задаем нолевой индекс для считывания элементов строки
new_s = ''                                          # создаем новую пустую строку, в которую будем записывать результат
while i < len(s):                                   # до тех пор, пока индекс меньше длины строки
    j = i + 1                                       # задаем индекс следующему элементу
    while j < len(s) and s[j].isdigit():            # то тех пор пока следующий элемент меньше длины строки и цифра
        j += 1                                      # увеличиваем значение на 1
    new_s = new_s + s[i] * int(s[i + 1:j])          # реультат записываем в новую строку
    i = j
with open('File2_for_3_9.txt', 'w') as out:         # открываем файл на запись
    out.write(new_s)                                # записываем нашу выходную строку в файл.

