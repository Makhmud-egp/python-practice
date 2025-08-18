class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance = {self.balance}")

    def get_balance(self):
        print(f"💰 Balance = {self.balance}")


# Example usage
if __name__ == "__main__":
    acc = BankAccount("Ali", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.get_balance()
