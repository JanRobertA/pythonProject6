#oppgavesett 4 oppgave 2

import datetime


class Transaction:
    def __init__(self, account_number, date, amount, type) -> None:
        self.account_number = account_number
        self.date = date
        self.amount = amount
        self.type = type

    def __str__(self):
        return f"Transaction(type={self.type}, amount={self.amount}, date={self.date})"


class BankAccount:
    def __init__(self, account_number, owner, initial_balance) -> None:
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = initial_balance
        self.__transactions = []
        self.__transactions.append(
            Transaction(
                account_number, datetime.datetime.now(), initial_balance, 'DEPOSIT'
            )
        )

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(
                Transaction(
                    self.__account_number, datetime.datetime.now(), amount, 'DEPOSIT'
                )
            )
            print(f'{amount} deposited successfully')
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount < 0 or amount > self.__balance:
            print(f'Not enough money. The amount is {amount} but balance is {self.__balance}')
            return
        self.__balance -= amount
        self.__transactions.append(
            Transaction(
                self.__account_number, datetime.datetime.now(), amount, 'WITHDRAW'
            )
        )
        print(f'{amount} withdrawn successfully')

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance must be positive.")

    def get_account_number(self):
        return self.__account_number

    def get_transactions(self):
        return self.__transactions

    def __str__(self):
        return f"BankAccount(account_number={self.__account_number}, owner={self.__owner}, balance={self.__balance})"


# Testkode
account = BankAccount('1234567890', 'Alice', 10000)
print(account.get_balance())
account.deposit(10000)
print(account.get_balance())
account.withdraw(152)
print(account.get_balance())

# Vis transaksjoner
transactions = account.get_transactions()
for transaction in transactions:
    print(transaction)
