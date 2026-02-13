# interface.py
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class CreditCard(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


if __name__ == "__main__":
    payments = [PayPal(), CreditCard()]

    for payment in payments:
        payment.pay(100)
