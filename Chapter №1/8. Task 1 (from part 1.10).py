# Пересып или недосып
recommend = int(input('Рекомендуется спать часов: '))
do_not_recommend = int(input('Не рекомендуется спать более часов: '))
anna_sleep = int(input('Аня спит часов: '))
if do_not_recommend >= recommend > anna_sleep:
    print('Недосып')
elif anna_sleep > do_not_recommend >= recommend:
    print('Пересып')
else:
    print('Это нормально')