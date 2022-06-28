'''Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность этого проекта — одежда (class Clothes). К типам одежды в этом проекте относятся пальто
(class Coat) и костюм (class Costume). У этих типов одежды существуют параметры: размер size (для пальто)
и рост height (для костюма). Значения параметров size и height, которые они могут принять предусмотреть как float.

Для определения расхода ткани по каждому типу одежды использовать формулы:

для пальто (size / 6.5 + 0.5),
для костюма (2 * height + 0.3),
расчёты расхода ткани производить в методе calculate, который должен возвращать float-значение с количеством
знаков после плавающей точки не более двух
Оформить код, используя декоратор абстрактного метода, чтобы регламентировать обязательное определение
в классах типов одежды метода calculate. Используйте декоратор @property для возможности обращения к методу calculate,
как к атрибуту класса.'''


from abc import ABC


class Clothes(ABC):
    def __init__(self, size):
        try:
            if isinstance(size, float) or isinstance(size, int):
                self.size = size
                self.height = size
            else:
                raise TypeError('TypeError, Val mast be float')
        except TypeError as e:
            print(f'{e} проверь вводимые данные')


class Coat(Clothes):
    @property
    def calculate(self):
        return (f'{self.size / 6.5 + 0.5:.2f}')


class Costume(Clothes):
    @property
    def calculate(self):
        return f'{2 * self.height + 0.3:.2f}'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3