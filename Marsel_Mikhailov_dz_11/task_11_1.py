'''Задание 1
Реализовать класс Дата, функция-конструктор которого должна принимать дату в виде строки формата день-месяц-год.
В рамках класса реализовать два метода:

Первый — с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


import re


class Date:
    date = None

    def __init__(self, date: str):
        '''проверяю с помощью регулярки правильность формата ввода даты'''
        try:
            regular = re.search(r'\d{2}-\d{2}-\d{4}', date)
            if regular.group() == date:
                Date.date = date
        except AttributeError as e:
            print(f'{e} Неверный формат даты: {date} !!!')

    @classmethod
    def int_date(cls) -> int:
        '''Если не прошла первая проверка, то в cls.date будет возвращаться None, чтоб дальше не выкидывало с программы,
        задаю условие на отлов исключения'''
        try:
            date_int = cls.date.split('-')
            date_int = int(''.join(date_int))
            return date_int
        except AttributeError as e:
            print(f'{e} Невозможно перевести в численный метод, не правильный формат')

    @staticmethod
    def check_date() -> str:
        '''С помощью срезов создаю дни, месяцы. задаю условия для количества дней и мес. На февраль создал отдельное условие
        для весокосного года)), так же проверяю на правильный формат, и создаю и отлавливаю исключения'''
        try:
            days = int(Date.date[:2])
            months = int(Date.date[3:5])
            if months > 12 or days > 31:
                raise TypeError(f'{Date.date} Невозможная дата!!!')
            elif months == 2 and days > 29:
                raise TypeError(f'{Date.date} Невозможная дата!!!')
        except TypeError as e:
            print(f'{e}')


if __name__ == '__main__':
    d1 = Date('31-02-1990')
    print(d1.int_date())
    Date.check_date()