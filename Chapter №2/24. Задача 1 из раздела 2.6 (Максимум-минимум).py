# Поиск минимума в списке
my_list = [int(i) for i in input().split()]
print(my_list)
m = my_list[0]
for i in my_list:
    if m > i:
        m = i
print(m)