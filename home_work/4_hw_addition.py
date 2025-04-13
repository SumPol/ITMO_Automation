class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print('Автомобиль заведен')

    def stop_car(self):
        print('Автомобиль заглушен')

    def set_year(self, year):
        self.year = year
        return self

    def set_type(self, type):
        self.type = type
        return self

    def set_color(self, color):
        self.color = color
        return self


car1 = Car('blue', 'sedan', 2019)

car1.start_car()
car1.stop_car()
print('\n')

print('Цвет ' + car1.color + ', ' + 'Тип ' + car1.type + ', ' + 'Год ' + str(car1.year))
car1.set_year(2025).set_type('supercar').set_color('red')
print('Цвет ' + car1.color + ', ' + 'Тип ' + car1.type + ', ' + 'Год ' + str(car1.year))