"""
File: bank_v2.py
Reengineered to support BankAccount hierarchy and polymorphic behavior.
"""
import pickle
 
class Bank:
    def __init__(self, fileName = None):
        """
        load the data from file if fileName is not None, 
        otherwise initialize an empty bank.
        capture EOFError 
        """
        self.accounts = {}
        self.fileName = fileName
        if fileName:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break
 
    def makeKey(self, name, pin, accountType):
        """Makes and returns a key from name, pin, and account type."""
        # Requirement: Append the account type to the existing key
        return f"{name}/{pin}/{accountType}"
 
    def add(self, account):
        """Inserts an account using its specific type in the key."""
        # Dynamically get the class name (e.g., 'SavingsAccount' or 'CheckingAccount')
        accountType = type(account).__name__
        key = self.makeKey(account.getName(), account.getPin(), accountType)
        self.accounts[key] = account
 
    def remove(self, name, pin, accountType):
        """Removes and returns the specific account type, or None."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.pop(key, None)
 
    def get(self, name, pin, accountType):
        """Returns the specific account type, or None."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.get(key, None)
 
    def computeInterest(self):
        """Polymorphically computes interest only for applicable accounts."""
        total = 0.0
        # Iterate through all accounts (Savings, Checking, Restricted)
        for account in self.accounts.values():
            # Check if the account object has the computeInterest method
            if hasattr(account, 'computeInterest'):
                total += account.computeInterest()
        return total
 
    def getKeys(self):
        """Returns a sorted list of all account keys."""
        return sorted(self.accounts.keys())
 
    def save(self, fileName = None):
        '''
        Saves the bank accounts to a file using pickle. If fileName is None, does nothing.
        '''
        if fileName:
            self.fileName = fileName
        if not self.fileName:
            return
        fileObj = open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
 
    def __str__(self):
        """Returns the string representation of all accounts."""
        if not self.accounts:
            return "The bank is empty."
        # Use the __str__ of each account (Checking or Savings)
        return "\n----------------\n".join(map(str, self.accounts.values()))
