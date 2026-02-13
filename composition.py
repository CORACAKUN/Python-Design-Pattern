# composition.py

class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, engine):
        self.engine = engine  # Car HAS an engine

    def start(self):
        return self.engine.start()


if __name__ == "__main__":
    engine = Engine()
    car = Car(engine)

    print(car.start())
