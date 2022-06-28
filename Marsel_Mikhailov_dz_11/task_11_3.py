'''Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду stop. При этом скрипт завершается,
сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести
текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.'''


class InvalidFormat(Exception):
    _information = 'InvalidFormat, необходимо вводить число'

    def __init__(self, information=None):
        if information:
            self._information = information

    def __str__(self):
        return self._information


some_list = []
while True:
    try:
        input_data = input('Ведите число: ')
        if input_data == 'stop':
            break
        elif isinstance(input_data, int) or isinstance(input_data, str):
            if input_data.isdigit():
                some_list.append(input_data)
            else:
                raise InvalidFormat
    except InvalidFormat as e:
        print(f'{e}')
print(some_list)