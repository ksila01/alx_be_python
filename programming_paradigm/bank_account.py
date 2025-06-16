# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Initialize account balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if amount > self.account_balance:
            return False  # Insufficient funds
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
