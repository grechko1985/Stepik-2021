# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза. Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
str = [int(i) for i in input().split()]                           # создаем список 1 - вводим его значения
ans = []                                                          # создаем новый список пустой
[ans.append(x) for x in str if x not in ans and str.count(x) > 1] # добавить x в ans если его нет в списке и счетчик > 1
print(*ans)
