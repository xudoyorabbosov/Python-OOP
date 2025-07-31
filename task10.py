class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Balans yetarli emas!")

acc = BankAccount("Ali", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
