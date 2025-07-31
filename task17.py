class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}: {self.balance}")

    def get_balance(self):
        return self.balance

accounts = [
    BankAccount("Ali", 150),
    BankAccount("Laylo", 200),
    BankAccount("John", 300),
    BankAccount("Malika", 250),
    BankAccount("Olim", 100)
]

total_balance = 0
for acc in accounts:
    total_balance += acc.get_balance()

print(f"Jami balans: {total_balance}")
