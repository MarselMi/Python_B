'''Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным целочисленным значением,
включая 0.'''


def val_checker(function):
    def inner(args):
        try:
            if args > 0 and isinstance(args, int) == True:
                print(function(args))
            else:
                raise (ValueError, TypeError)
        except TypeError as e:
            print(f'{e}: Val Error {args}')
    return inner


@val_checker
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    calc_cube(10)
    calc_cube('ss')
    calc_cube(-6)
    calc_cube(8.2)