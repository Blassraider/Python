"""
File: bank.py
A simplified version of the Bank class focusing on polymorphism 
and the BankAccount hierarchy.
"""

class Bank:
    def __init__(self):
        """Initializes an empty bank."""
        self.accounts = {}

    # note the key is updated to reflect the account type.
    def makeKey(self, name, pin, accountType):
        """Creates a unique key by appending the account type."""
        return f"{name}/{pin}/{accountType}"

    def add(self, account):
        """Adds an account to the bank using a type-aware key."""
        # Get the class name dynamically (CheckingAccount, SavingsAccount, etc.)
        acc_type = type(account).__name__
        key = self.makeKey(account.getName(), account.getPin(), acc_type)
        self.accounts[key] = account

    def get(self, name, pin, accountType):
        """Retrieves a specific account type."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.get(key, None)

    def remove(self, name, pin, accountType):
        """Removes and returns a specific account type."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.pop(key, None)

    # note the polymorphic behavior in this method.
    def computeInterest(self):
        """
        Polymorphically computes interest.
        Only calls computeInterest on objects that have the method.
        """
        total = 0.0
        for account in self.accounts.values():
            if hasattr(account, 'computeInterest'):
                total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys currently in the bank."""
        return sorted(self.accounts.keys())

    def __str__(self):
        """Returns a string representation of all accounts."""
        if not self.accounts:
            return "The bank is empty."
        # Sort by keys to keep the output predictable
        sorted_keys = self.getKeys()
        return "\n----------------\n".join([str(self.accounts[k]) for k in sorted_keys])
