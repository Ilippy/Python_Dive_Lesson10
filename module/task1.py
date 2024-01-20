# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * self.pi * self.radius

    def get_circle_area(self):
        return self.pi * self.radius ** 2
