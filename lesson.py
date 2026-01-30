class Car:
    def __init__(self, name, engine, year):
        self.name = name
        self.engine = engine
        self.year = year
        self.maxspeed = 360

    def info(self):
        return f'Машина {self.name} обьем двигателя: {self.engine}, год выпуска: {self.year}, максимальная скорость {self.maxspeed}'

a = Car('Mersedes', '5.5', 2024)
print(a.info())