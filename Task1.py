class BankAccount:
    """
    A class representing a bank account with attributes for account holder name, account number, and balance,
    and methods to deposit, withdraw, and display the current balance.
    """

    def __init__(self, account_holder_name, account_number, balance=0.0):
        """
        Initializes a BankAccount object with the given account holder name, account number, and balance.
        """
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the given amount to the account balance.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount:.2f} to account {self.account_number}.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account balance, checking for sufficient funds.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew Rs {amount:.2f} from account {self.account_number}.")
            else:
                print(f"Insufficient funds in account {self.account_number}. Available balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance

    def __str__(self):
        """
        Returns a string representation of the BankAccount object.
        """
        return f"Account Holder: {self.account_holder_name}\nAccount Number: {self.account_number}\nBalance: Rs {self.balance:.2f}"


account1 = BankAccount("Lahari", "1234567890", 100.00)
account1.deposit(50.00)
account1.withdraw(25.00)
account1.withdraw(100.00)  # Insufficient funds
print(account1)
