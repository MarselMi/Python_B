'''Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать в stdout информацию по формату
(формат сообщений смотрите в документации методов исходного задания);
значение аргумента direction, передаваемого в метод turn(direction) может иметь только одно из четырез значений:
направо, налево, прямо или назад (если передать другое значение, то должно быть возбуждено исключение ValueError
с сообщением нераспознанное направление движения)
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля по формату
в документации метода, если атрибут is_police равен True, то при вызове метода выводить в stdout дополнительно
второе сообщение Вруби мигалку и забудь про скорость!;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
в stdout должно выводиться сообщение о превышении скорости Alarm!!! Speed!!!, если превышения нет, то стандартное
сообщение из родительского класса.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''


class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        self.speed += 15
        return print(f'Машина {self.name} повысила скорость на 15: {self.speed}')

    def stop(self) -> None:
        stop = self.speed - self.speed
        return print(f'{self.name}: остановилась, скорость равна = {stop}')

    def turn(self, direction: str) -> None:
        turn_auto = {'налево', 'направо', 'вперед', 'назад'}
        if direction in turn_auto:
            print(f'{self.name}({self.__class__.__name__}): движется {direction}')
        else:
            print('ValueError')

    def show_speed(self) -> None:
        return print(f'{self.name}: текущая скорость {self.speed} км/час')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print('Alarm!!! Speed!!!')
        else:
            Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('Alarm!!! Speed!!!')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def show_speed(self):
        pass


class PoliceCar(Car):
    Car.is_police = True
    def show_speed(self) -> None:
        super().show_speed()
        if Car.is_police is not False:
            print('Вруби мигалку и забудь про скорость!')


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """
