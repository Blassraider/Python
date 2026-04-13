"""
File: checkingaccount.py
This module defines the CheckingAccount class.
CheckingAccount does not have interest.
"""

class CheckingAccount:
    """This class represents a checking account with name, PIN, and balance."""

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        """This deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if was successful, or an
        error message if was unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def getBalance(self):
        """This returns the current balance."""
        return self.balance

    def getName(self):
        """This returns the current name."""
        return self.name

    def getPin(self):
        """This returns the current pin."""
        return self.pin

    def __str__(self):
        """This returns the string rep."""
        result =  'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result


def main():
    """Tests the CheckingAccount class to cover the following cases:
    # 1. Test Instantiation
    # 2. Test String Representation (__str__)
    # 3. Test Getters
    # 4. Test Deposit
    # 5. Test Withdrawals
    #    - Successful withdrawal
    #    - Insufficient funds
    #    - Negative amount
    # 6. Final State
    """

    # 1. Test Instantiation
    account = CheckingAccount("Jaylen Stingley", "2222", 500.0)
    print("Account created:", account.getName())

    # 2. Test String Representation (__str__)
    print(account)

    # 3. Test Getters
    print(account.getName())
    print(account.getPin())
    print(account.getBalance())

    # 4. Test Deposit
    account.deposit(200.0)
    print(account.getBalance())

    # 5. Test Withdrawals
    # Successful withdrawal
    print(account.withdraw(100.0))

    # Insufficient funds
    print(account.withdraw(10000.0))

    # Negative amount
    print(account.withdraw(-50.0))

    # 6. Final State
    print(account)


if __name__ == "__main__":
    main()
