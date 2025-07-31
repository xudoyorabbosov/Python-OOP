class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Yetarli mablag' yo'q")

    def show_balance(self):
        print(f"{self.owner}ning balansi: {self.balance}")

acc1 = BankAccount("Ali", 100)
acc2 = BankAccount("Laylo", 200)
acc3 = BankAccount("John", 150)

acc1.deposit(50)
acc2.withdraw(30)
acc3.deposit(70)

acc1.show_balance()
acc2.show_balance()
acc3.show_balance()
