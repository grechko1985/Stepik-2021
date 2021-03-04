# https://www.youtube.com/watch?v=VfXdU0YIVLA
arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(arr_2d)
print(arr_2d[0][2])

arr_2d_2 = [
    [1, 2, 3],
    [4, 5, 6, -1, -7],
    [7]]
print(arr_2d_2)

def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()
print(print_matrix(arr_2d))

def print_matrix_new(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end=' ')
        print()
print(print_matrix_new(arr_2d))

# Обновление элементов в списке
arr_2d[1][1] = 100
print(print_matrix_new(arr_2d))

# Задача 1 - создание двумерного массива и панолнение нолями
arr_2d_1 = []
m = int(input('Введите количество строк m: '))
n = int(input('Введите количество столбцов n: '))
for i in range(m):
    internal_arr = []
    for j in range(n):
        internal_arr.append(0)
    arr_2d_1.append(internal_arr)
print(arr_2d_1)