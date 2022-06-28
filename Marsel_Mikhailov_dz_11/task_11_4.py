'''Начать работу над проектом Склад оргтехники.

Создать класс, описывающий склад. А также класс Оргтехника, который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (Принтер, Сканер, Ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над заданием 4.

Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
Продолжить работу над заданием 5.

Реализовать механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных!'''


class OfficeEquipment:

    def __init__(self, mass: float, volume: float, list_count: set):
        self.list_count = list_count
        self.list_count.add(self)
        try:
            if isinstance(mass, float) or isinstance(mass, int) and isinstance(volume, float) or isinstance(volume, int):
                self.mass = mass
                self.volume = volume
            else:
                raise TypeError
        except TypeError as e:
            print(f'\nВ {self.__class__.__name__} Неверные данные {e}\n')

    def count(self):
        print(f'Всего {self.__class__.__name__} поступило в количестве - {len(self.list_count)} шт.\n')

    '''знаю что суммирование не реализуют таким образом, указал для нагоядности'''
    def __add__(self, other):
        volume = self.volume + other.volume
        mass = self.mass + other.mass
        return f'{volume:.2f} - суммарный обьем, {mass:.2f} - суммарная масса'

    def discharge(self):
        self.list_count.discard(self)


scan_set = set()


class Scanner(OfficeEquipment):

    def __init__(self, mass: float, volume: float, color: str, list_count: set):
        super().__init__(mass, volume, list_count)
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__}: Вес = {self.mass} кг., Обьем = {self.volume} куб. м., Цвет = {self.color}'


xerox_set = set()


class Xerox(OfficeEquipment):

    def __init__(self, mass: float, volume: float, method: str, list_count: set):
        super().__init__(mass, volume, list_count)
        self.method = method

    def __str__(self):
        return f'{self.__class__.__name__}: Вес = {self.mass} кг., Обьем = {self.volume} куб. м., Принцип работы = {self.method}'


printer_set = set()


class Printer(OfficeEquipment):

    def __init__(self, mass: float, volume: float, method: str, list_count: set):
        super().__init__(mass, volume, list_count)
        self.method = method

    def __str__(self):
        return f'{self.__class__.__name__}: Вес = {self.mass} кг., Обьем = {self.volume} куб. м., Принцип работы = {self.method}'


class WareHouse():
    max_xerox_count = 40
    max_printer_count = 40
    max_scanner_count = 40

    def xerox_save(self):
        print(f'В отдел ксерокса поступило: {len(xerox_set)} шт. новых аппаратов\nсвободного места осталось: {self.max_xerox_count - len(xerox_set)} шт.\n')

    def printer_save(self):
        print(f'В отдел принтеров поступило: {len(printer_set)} шт. новых аппаратов\nсвободного места осталось: {self.max_printer_count - len(printer_set)} шт.\n')

    def scanner_save(self):
        print(f'В отдел сканеров поступило: {len(scan_set)} шт. новых аппаратов\nсвободного места осталось: {self.max_scanner_count - len(scan_set)} шт.\n')

    def count(self):
        return f'В общем на складе находится: {len(scan_set) + len(xerox_set) + len(printer_set)} наименований\n' \
               f'свободного места на складе для новых поступлений осталось: ' \
               f'{(self.max_xerox_count + self.max_printer_count + self.max_scanner_count) - (len(scan_set) + len(xerox_set) + len(printer_set))} '


if __name__ == '__main__':
    wh = WareHouse()
    scanner_1 = Scanner(2.3, 0.6, 'black', scan_set)
    scanner_2 = Scanner(1.8, 0.3, 'white', scan_set)
    scanner_3 = Scanner(2.0, 0.2, 'grey', scan_set)
    scanner_4 = Scanner(4, 0.6, 'grey', scan_set)
    scanner_5 = Scanner(2.1, 0.3, 'white', scan_set)
    scanner_6 = Scanner(2.0, 0.2, 'grey', scan_set)
    print('Какие сканеры у нас есть!')
    for s in scan_set:
        print(f'\t{s}')
    scanner_6.count()
    xerox_1 = Xerox(1.8, 0.2, 'автоматический', xerox_set)
    xerox_2 = Xerox(1.7, 0.25, 'ручной', xerox_set)
    xerox_3 = Xerox(1.8, 0.2, 'автоматический', xerox_set)
    xerox_4 = Xerox(1.7, 0.25, 'ручной', xerox_set)
    print('Какие ксероксы у нас есть!')
    for s in xerox_set:
        print(f'\t{s}')
    xerox_4.count()

    printer_1 = Printer(2.3, 0.3, 'струйный', printer_set)
    printer_2 = Printer(2.4, 0.4, 'лазерный', printer_set)
    printer_3 = Printer(1.5, 0.25, 'струйный', printer_set)
    printer_4 = Printer(1.8, 0.3, 'струйный', printer_set)
    printer_5 = Printer(1.9, 0.3, 'лазерный', printer_set)
    print('Какие принтеры у нас есть!')
    for s in printer_set:
        print(f'\t{s}')
    printer_5.count()

    wh.xerox_save()
    wh.printer_save()
    wh.scanner_save()
    print(wh.count())
    print(f'сумма: {printer_1 + printer_2}')
    print(f'сумма: {xerox_1 + xerox_3}')
    print('')

    printer_2.discharge() # не пойму почему в список выводятся принтеры не по порядку их определения
    print('Какие принтеры теперь у нас остались!')
    for s in printer_set:
        print(f'\t{s}')
    printer_1.count()

    def mass_calculation(set):
        mass = 0
        for item in set:
            mass += item.__dict__['mass']
        return f'общая масса {item.__class__.__name__}: {mass:.2f} кг.'

    def volume_calculate(set):
        volume = 0
        for item in set:
            volume += item.__dict__['volume']
        return f'общий обьем {item.__class__.__name__}: {volume:.2f} кубометров'

    print(volume_calculate(printer_set))
    print(volume_calculate(xerox_set))
    print(volume_calculate(scan_set))
    print('')
    print(mass_calculation(printer_set))
    print(mass_calculation(scan_set))
    print(mass_calculation(xerox_set))


print('end')