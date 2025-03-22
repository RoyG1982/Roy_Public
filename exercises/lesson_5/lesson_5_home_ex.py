import random
class bank_account():

    def __init__(self, first_name, last_name, address, account_number, balance, currency):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def convert_currency(self, amount):
        if self.currency == "USD":
            return amount
        elif self.currency == "EUR":
            return amount * 0.96
        elif self.currency == "ILS":
            return amount * 3.59

    def deposit(self, amount):
        amount = self.convert_currency(amount)
        self.balance = self.balance + amount
        print (f"amount was deposited successfully, {self.first_name}")
        return (amount)

    def withdraw(self, amount):
        amount = self.convert_currency(amount)
        self.balance = self.balance - amount
        print (f"amount was withdrawn successfully, {self.first_name}")
        return (amount)

    def check_balance(self):
        print(f"account number {self.account_number},{self.balance}")

John = bank_account ("John", "Wane", "Hollywood", random.randint(100000, 999999), 0, "ILS")
Michael = bank_account ("Michael", "Caine", "London", random.randint(100000, 999999), 0, "ILS")

John.deposit(2)
John.withdraw(1)
John.check_balance()

Michael.deposit(2)
Michael.withdraw(1)
Michael.check_balance()