class Car:

    def __init__(self, color: str, type: str, year: int):
        self.color = color
        self.type = type
        self.year = year

    def car_on(self):
        print('Автомобиль заведен')

    def car_off(self):
        print('Автомобиль заглушен')

    def car_year(self):
        self.year = input('Введите год выпуска: ')
        return self.year

    def car_type(self):
        self.type = input('Введите тип автомобиля: ')
        return self.type

    def car_color(self):
        self.color = input('Введите цвет автомобиля: ')
        return self.color


car = Car('красный', 'хэтчбек', 2001)

print(car.year)
print(car.type)
print(car.color)
car.car_year()
car.car_type()
car.car_color()
print(car.year)
print(car.type)
print(car.color)
