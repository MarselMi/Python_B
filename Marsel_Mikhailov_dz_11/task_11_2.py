'''Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ZeroErr(ZeroDivisionError):
    _information = 'Zero division Error / (ошибка деления на ноль)'

    def __init__(self, information=None):
        if information:
            self._information = information

    def __str__(self):
        return self._information


def division(a: int, b: int):
    try:
        if b == 0:
            raise ZeroErr
        print(a / b)
    except ZeroErr as e:
        print(e)


if __name__ == '__main__':
    division(10, 0)
