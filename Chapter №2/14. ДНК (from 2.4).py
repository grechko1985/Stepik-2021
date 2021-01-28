# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы
# информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
# символ и количество его повторений в этой позиции строки.
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
dnk = input('Введите ДНК содержащий ТОЛЬКО символы a, b и с: ')
i = 0
while i != len(dnk):
    if dnk[i] == 'a':
        sum_a = 0
        while dnk[i] == 'a':
            sum_a += 1
            i += 1
            if i == len(dnk):
                break
        print('a' + str(sum_a), end='')
    elif dnk[i] == 'b':
        sum_b = 0
        while dnk[i] == 'b':
            sum_b += 1
            i += 1
            if i == len(dnk):
                break
        print('b' + str(sum_b), end='')
    elif dnk[i] == 'c':
        sum_c = 0
        while dnk[i] == 'c':
            sum_c += 1
            i += 1
            if i == len(dnk):
                break
        print('c' + str(sum_c), end='')
    elif dnk[i] == 'A':
        sum_A = 0
        while dnk[i] == 'A':
            sum_A += 1
            i += 1
            if i == len(dnk):
                break
        print('A' + str(sum_A), end='')
    elif dnk[i] == 'B':
        sum_B = 0
        while dnk[i] == 'B':
            sum_B += 1
            i += 1
            if i == len(dnk):
                break
        print('B' + str(sum_B), end='')
    elif dnk[i] == 'C':
        sum_C = 0
        while dnk[i] == 'C':
            sum_C += 1
            i += 1
            if i == len(dnk):
                break
        print('C' + str(sum_C), end='')
    else:
        break
