# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from module.task3 import Human


# import itertools


class Employee(Human):
    # id_iter = itertools.count(1_000_000_000_000_000)
    class_id = 1_000_000_000_000_000

    def __init__(self, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)
        # self.id = next(self.id_iter)
        self.id = self.class_id
        Employee.class_id += 1

    def get_access_level(self):
        return sum(map(int, str(self.id))) % 7

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.age} лет. Уровень доступа {self.get_access_level()}"
