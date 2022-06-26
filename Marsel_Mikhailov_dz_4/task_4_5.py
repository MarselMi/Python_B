'''*(вместо 4) Рядом со скриптом task_4_4.py, создать скрипт task_4_5.py
с содержимым аналогичным task_4_4.py, но переработанным так,
чтобы новый скрипт теперь срабатывал, как CLI, прямо в консоли/терминале.
Например:
>python task_4_5.py USD
75.18, 2020-09-05 '''


import sys
import requests


'''Назначаю константные переменные'''
REQ = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
CONTENT = REQ.text
DATE_NOW = CONTENT.split('ID=')[0][54:71]
LIST_WITH_VALUES = CONTENT.split('<Valute ID="')[1:]


def currency_rates(val: str):
    '''Функция для парсинга данных о курсах валют'''
    val = val.upper()
    for sim in LIST_WITH_VALUES:
        if val in sim:
            nominal = sim[sim.index('<Nominal>') + 9:sim.index('</Nominal>')]
            val_price = sim[sim.index('<Value>') + 7:sim.index('</Value')].replace(',', '.')
            return f'At {DATE_NOW} {val} = {float(val_price) / int(nominal)}'


val = sys.argv[1]


if __name__ == '__main__':
    print(currency_rates(val))