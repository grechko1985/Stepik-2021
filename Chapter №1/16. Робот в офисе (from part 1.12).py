# Робот в офисе - n програмистов, n программиста, n программист
students = int(input('Введите количество студентов в аудитории: '))
if students % 10 == 1 and students % 100 != 11 and students % 100 != 12 and students % 100 != 13 and \
        students % 100 != 14 and students % 100 != 15 and students % 100 != 16 and students % 100 != 17 and \
        students % 100 != 18 and students % 100 != 19:
    print(students, 'программист')
elif (students % 10 == 2 or students % 10 == 3 or students % 10 == 4) and students % 100 != 12 and \
        students % 100 != 13 and students % 100 != 14:
    print(students, 'программиста')
else:
    print(students, 'программистов')
