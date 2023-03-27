from datetime import datetime, timezone


class OverdraftNotAllowed(ValueError):
    pass


class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance, is_overdraft_allowed):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = balance
        self._is_overdraft_allowed = is_overdraft_allowed
        self._ledger = []

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def is_overdraft_allowed(self):
        return self._is_overdraft_allowed

    @is_overdraft_allowed.setter
    def is_overdraft_allowed(self, value):
        self._is_overdraft_allowed = value

    def __str__(self):
        return f'{self._first_name} {self._last_name} ({self._account_number}): {self._balance}'

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('the value must be positive')
        if self._balance < amount and not self._is_overdraft_allowed:
            raise OverdraftNotAllowed('there are not enough funds on the account')
        s = str(datetime.now(timezone.utc).replace(tzinfo=None)) + ' -' + str(amount)
        self._ledger.append(s)
        self._balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('the value must be positive')
        s = str(datetime.now(timezone.utc).replace(tzinfo=None)) + ' ' + str(amount)
        self._ledger.append(s)
        self._balance += amount

    @property
    def ledger(self):
        return self._ledger
    
    def __eq__(self, other):
        if isinstance(other, BankAccount) and self._account_number == other._account_number:
            return True
        return False
        




ba = BankAccount('Ivan', 'Petrov', 34553, 10000, True)
ba2 = BankAccount('Ivan2', 'Petrov2', 34553, 1110000, True)
ba3 = BankAccount('Ivan2', 'Petrov2', 134553, 1110000, True)
print(ba.is_overdraft_allowed)
# ba.is_overdraft_allowed = False
print(ba.is_overdraft_allowed)
print(ba)
# ba.deposit(-100)
ba.deposit(100)
print(ba)
ba.withdraw(10000)
# ba.withdraw(200)
ba.withdraw(10000)
print(ba)
print(ba.ledger)
print(ba == ba2)
print(ba == ba3)
print(ba == 'test')
