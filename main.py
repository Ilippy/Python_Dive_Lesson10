import module


# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
def task1():
    # circle = module.task1.Circle(5)
    Circle = type('Circle', (object,), {
        'pi': 3.14,
        '__init__': lambda self, radius: setattr(self, 'radius', radius),
        'get_circumference': lambda self: 2 * self.pi * self.radius,
        'get_circle_area': lambda self: self.pi * self.radius ** 2
    })
    circle = Circle(2)
    print(circle.__dict__)
    print("Площадь окружности =", circle.get_circle_area())
    print(f"Длина окружности = {circle.get_circumference(): .2f}")


# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
def task2():
    rectangle = module.task2.Rectangle(5)
    print("Периметр прямоугольника =", rectangle.get_perimeter())
    print("Площадь прямоугольника =", rectangle.get_area())


# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
def task3():
    human = module.task3.Human("Иван", "Иванов", 36)
    print(human.full_name())
    print(human.age)
    human.birthday()
    print(human.age)
    try:
        human.age = 35
    except AttributeError as e:
        print(e)


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
def task4():
    employee = module.task4.Employee("Иван", "Иванов", 15)
    print(employee)
    employee2 = module.task4.Employee("Илья", "Куликоский", 36)
    print(employee2)


def main():
    # task1()
    # task2()
    # task3()
    task4()


if __name__ == '__main__':
    main()
