import pytest


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'The car is being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(self.driver)

    def drive(self):
        if self.driver.age > 16:
            self._car.drive()
            return
        raise Exception('Driver too young to drive')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def test_driver_can_drive_both_cars():
    driver = Driver('Mark', 20)
    car = Car(driver)
    car_proxy = CarProxy(driver)
    car.drive()
    car_proxy.drive()


def test_young_driver_can_drive_car():
    driver = Driver('Mark', 10)
    car = Car(driver)
    car.drive()


def test_young_driver_cant_drive_carproxy():
    driver = Driver('Mark', 10)
    car = CarProxy(driver)
    with pytest.raises(Exception):
        car.drive()
