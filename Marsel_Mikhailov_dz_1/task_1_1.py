''' Реализовать вывод информации о промежутке времени в зависимости
от его продолжительности duration в секундах'''

duration = 8153
days = duration // 86400
hours = duration % 86400 // 3600
mins = duration % 3600 // 60
secs = duration % 60
if duration < 60:
    print(f'{secs} сек')
elif duration < 3600:
    print(f'{mins} минут {secs} сек')
elif duration < 86400:
    print(f'{hours} час {mins} минут {secs} сек')
else:
    print(f'{days} дн. {hours} час {mins} минут {secs} сек')