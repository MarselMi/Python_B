'''Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов'''


def transform_string(n: int) -> str:
    if int(str(n)[-1]) == 1:
        return f'{n} процент'
    elif 1 < int(str(n)[-1]) < 5:
        return f'{n} процента'
    else:
        return f'{n} прооцентов'

for n in range(1, 101):
    print(transform_string(n))