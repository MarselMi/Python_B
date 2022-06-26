'''В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и
возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.

Подумайте:
есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.'''


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


val = 'eur'

if __name__ == '__main__':
    currency_rates(val)