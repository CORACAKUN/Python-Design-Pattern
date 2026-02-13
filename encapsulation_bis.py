# encapsulation_bis.py

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount")


if __name__ == "__main__":
    account = BankAccount(1000)

    print(account.balance)
    account.balance = 2000
    print(account.balance)
