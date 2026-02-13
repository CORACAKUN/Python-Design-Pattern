# interface_bis.py

class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def make_sound(animal):
    print(animal.speak())


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    make_sound(dog)
    make_sound(cat)
