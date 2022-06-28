'''Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

$ a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

$ a = calc_cube(5)
calc_cube(5: <class 'int'>)'''


from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}', end='')
        print(f'{"("}{args[0]}:', type(args[0]), end='')
        if len(args) != 1:
            for arg in args[1:]:
                print(f', {arg}:', type(arg), end='')
        if len(kwargs):
            for key, item in kwargs.items():
                print(f', {key}={item}:', type(item), end='')
        print(f'{")"} -> {result}:', type(result))
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)