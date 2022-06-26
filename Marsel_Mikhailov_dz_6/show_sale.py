'''Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1'''


import sys


def show_sales():
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        if len(sys.argv) == 3:
            out = fr.readlines()[int(sys.argv[1]) - 1:int(sys.argv[2])]
            print(''.join(out))
        elif len(sys.argv) == 2:
            out = fr.readlines()[int(sys.argv[1]) - 1:]
            print(''.join(out))
        else:
            print(''.join(fr.readlines()))


if __name__ == '__main__':
    show_sales()