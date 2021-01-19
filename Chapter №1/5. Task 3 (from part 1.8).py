time = int(input())
print('Катя спит', time, 'минут.')
hours = int(input())
minutes = int(input())
hours_in_minutes = hours * 60
total_minutes = time + hours_in_minutes + minutes
print(total_minutes)
clock_hours = total_minutes // 60
clock_minutes = total_minutes % 60
print(clock_hours)
print(clock_minutes)