'''Реализовать базовый класс Worker (работник):

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.'''


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name.title() # перевожу первую букву в верхний регистр
        self.surname = surname.title() # перевожу первую букву в верхний регистр
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self) -> str:
        return self.name + ' ' + self.surname

    def get_total_income(self) -> int:
        return sum(self._income.values())


if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())
    print(driver.get_full_name(), driver.get_total_income())
    print(scientist.get_full_name(), scientist.get_total_income())
