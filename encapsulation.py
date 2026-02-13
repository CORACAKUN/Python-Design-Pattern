# encapsulation.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private variable

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age


if __name__ == "__main__":
    p = Person("Coraca", 20)

    print(p.get_age())
    p.set_age(25)
    print(p.get_age())
