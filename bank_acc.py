class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError

        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def transfer(self, other: BankAccount, amount):
        if not isinstance(other, BankAccount):
            raise TypeError
        self.withdraw(amount)
        other.deposit(amount)
        self.history.pop()
        other.history.pop()
        self.history.append(("transfer_out", amount))
        other.history.append(("transfer_in", amount))


acc = BankAccount("Dylan", 100)
other = BankAccount("friend", 0)

acc.transfer(other, 50)

print(acc.balance)
print(other.balance)
        