'''Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы. В случае если список списков некорректный - возбуждать исключение
ValueError с сообщением fail initialization matrix.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 43 |
| 22 51 |
| 37 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде (как показано выше).
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и пр.'''


from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        try:
            i = 0
            '''условие для проверки матрицы на предмет что она является матрицей, то есть строки матрицы равны по длинне'''
            while i < (len(matrix) - 1):
                if len(matrix[i]) == len(matrix[i + 1]):
                    self.matrix = matrix
                else:
                    raise ValueError(f'неправильная конструкция')
                i += 1
        except ValueError as e:
            print(f'{e} fail initialization matrix is: {matrix}')

    def __add__(self, other):
        '''проверка матриц на возможность суммирования между собой'''
        try:
            '''проверка длинны матриц, из скольки списков они состоят'''
            if len(self.matrix) == len(other.matrix):
                '''далее проверяю длинну первого списка матрицы. Проверяю первый список, потому что в __init__ уже была проверка
                на то чтобы все элементы в матрице имели одинаковую длинну'''
                if len(self.matrix[0]) == len(other.matrix[0]):
                    result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                              range(len(self.matrix))]
                else:
                    raise ValueError(f'неправильная конструкция')
            else:
                raise ValueError(f'неправильная конструкция')
        except ValueError as e:
            print(f'{e} матрицы должны быть одинковыми')

        new = ''
        for i in result:
            new += ('|' + str(i).strip('[]').replace(',', '') + '|\n')
        return new

    def __str__(self):
        new = ''
        for i in self.matrix:
            new += ('|' + str(i).strip('[]').replace(',', '') + '|\n')
        return new


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6], [2]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """