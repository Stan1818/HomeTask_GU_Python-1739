duration = int(input('Ведите количество секунд: '))
s1, s2, s3, s4 = duration, duration, duration, duration
s5 = 0
s6 = 0
if duration >= 86400:
    s1 = s1 // 86400
    s2 = s2 % 86400
    s3 = s2 // 3600
    s4 = s2 % 3600
    s5 = s4 // 60
    s6 = s4 % 60
    print(f'{duration} сек. это - {s1} день {s3} час {s5} минут {s6} секунд')

elif duration >= 3600 and duration < 86400:
    s3 = s2 // 3600
    s4 = s2 % 3600
    s5 = s4 // 60
    s6 = s4 % 60
    print(f'{duration} сек. это - {s3} час {s5} минут {s6} секунд')

elif duration >= 60 and duration < 3600:
    s5 = s4 // 60
    s6 = s4 % 60
    print(f'{duration} сек. это - {s5} минут {s6} секунд')

elif duration < 60:
    print(duration, 'секунд')
