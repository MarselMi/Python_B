'''Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и
для вывода на экран записанных данных. При записи передавать из командной строки
значение суммы продаж

python add_sale.py 5978,5'''


import sys


sale_price = sys.argv[1]


def write_sale():
    with open('bakery.csv', 'a', encoding='utf-8') as fw:
        fw.write(f'{sale_price}\n')


if __name__ == '__main__':
    write_sale()