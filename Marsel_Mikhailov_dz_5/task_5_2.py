'''*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield'''


def gen_num(number: int):
    '''Функция генерирующая нечетные цифры до n без использования yield'''
    nums = map(int, range(1, number + 1, 2))
    return nums


n = 15
gener = gen_num(n)


for _ in range(1, n + 1, 2):
    print(next(gener))
# print(next(gener)) #При раскомментировании выпадает трейсбэк StopIteration. Что доказывает работу генератора
