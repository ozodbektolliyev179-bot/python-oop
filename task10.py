class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Balans yetarli emas")


acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
