'''Реализовать проект Операции с комплексными числами.

Создать класс Комплексное число.
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.'''


class ComplexNumber:

    def __init__(self, number: int, complex: str):
        '''проверяю правильность ввода комплексного числа'''
        if isinstance(number, int) and isinstance(int(complex[:-1]), int) and complex[-1] == 'i':
            self.number = number
            self.complex = complex
        else:
            raise TypeError('Неверный формат ввода комплексного числа!!!')

    def __add__(self, other):
        if isinstance(self, ComplexNumber) and isinstance(other, ComplexNumber):
            complex_sum = int(self.complex[:-1]) + int(other.complex[:-1])
            complex = str(f'{complex_sum}i')
            return self.number + other.number, complex
        else:
            raise TypeError (f'Метод сложения только для обьектов класса {self.__class__.__name__}')

    def __mul__(self, other):
        if isinstance(self, ComplexNumber) and isinstance(other, ComplexNumber):
            number_mul = self.number * other.number + int(self.complex[:-1]) * int(other.complex[:-1]) * (-1)
            complex_mul = int(self.complex[:-1]) * other.number + self.number * int(other.complex[:-1])
            complex = str(f'{complex_mul}i')
            return number_mul, complex
        else:
            raise TypeError (f'Метод умножения только для обьектов класса {self.__class__.__name__}')

    def __str__(self):
        return f'{self.number, self.complex}'


if __name__ == '__main__':
    '''Комплексные числа следует вводить через запятую => (+-вещ. число, +-мним. число) знак плюс ставить необязательно
    Если в числе дискриминанта отсутствует мнимое число, для корректной работы программы его необходимо 
    передавать, как "0i", то же самое для вещественного числа, при его отсутствии нужно передать "0" '''

    complex_1 = ComplexNumber(+2, '+1i')
    complex_2 = ComplexNumber(2, '-2i')
    print(complex_2 + complex_1)
    print(complex_2 * complex_1)
    spy = (2, '3i')
    #print(complex_2 + spy)
    #print(complex_2 * spy)