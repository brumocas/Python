class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance

# Creating objects
account1 = BankAccount("John Doe", 1000)

# Accessing and modifying through methods
account1.deposit(500)
account1.withdraw(200)
print(f"Balance: ${account1.get_balance()}")
