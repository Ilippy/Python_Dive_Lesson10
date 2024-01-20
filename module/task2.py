# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length: int | float, width: int | float = None):
        self.length = length
        self.width = width if width else length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.length)
