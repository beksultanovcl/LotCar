class Car:
    def __init__(self, name, engine, year):
        self.name = name
        self.engine = engine
        self.year = year
        self.maxspeed = 360

    def info(self):
        return f'Машина {self.name} обьем двигателя: {self.engine}, год выпуска: {self.year}, максимальная скорость {self.maxspeed}'

class Big(Car):
    def __init__(self, name, engine, year):
        Car.__init__(self, name, engine, year)
        self.maxspeed = 360
        if self.engine >= 4.5:
            print(f'Большая машина {self.name}')
    def info(self):
        return f'Машина {self.name} обьем двигателя: {self.engine}, год выпуска: {self.year}, максимальная скорость {self.maxspeed}'
