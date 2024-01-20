class Human:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name, self.last_name, self.__age = first_name, last_name, age

    @property
    def age(self):
        return self.__age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def birthday(self):
        self.__age += 1
