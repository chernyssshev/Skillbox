from typing import Union


class Property:
    def __init__(self, worth: Union[int, float]):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth: Union[int, float]):
        super().__init__(worth)

    def tax(self) -> float:
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth: Union[int, float]):
        super().__init__(worth)

    def tax(self) -> float:
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth: Union[int, float]):
        super().__init__(worth)

    def tax(self) -> float:
        return self.worth / 500


while True:
    try:
        answer = int(input(' Имущество \n' +
                           ' 1 - Дом\n' +
                           ' 2 - Автомобиль\n' +
                           ' 3 - Дача\n' +
                           ' 0 - Выход\n ᐳ '))
        if answer not in (1, 2, 3, 0):
            raise ValueError
        if not answer:
            break
        cash = float(input('Имеющиеся средства: '))
        worth = float(input('Стоимость: '))
        error_data = False
    except ValueError:
        print('Ошибка. Попробуйте ещё раз.\n')
        error_data = True

    if not error_data:
        obj = Apartment(worth) if answer == 1 \
            else Car(worth) if answer == 2 \
            else CountryHouse(worth)
        print('\nНалог:', obj.tax(),
              'Необходимо ещё денег:',
              '-' if cash - obj.tax() >= 0 else obj.tax() - cash, '\n')
