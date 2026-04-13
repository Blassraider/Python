class BankAccount:
    """This class represents a bank account
    with the owner's name, PIN, and balance."""
 
    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
 
    def deposit(self, amount):
        """This deposits the given amount and returns None."""
        self.balance += amount
        return None
 
    def withdraw(self, amount):
        """This withdraws the given amount.
        It returns None if successful, or returns an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None
 
    def getBalance(self):
        """It returns the current balance."""
        return self.balance
 
    def getName(self):
        """It returns the current name."""
        return self.name
 
    def getPin(self):
        """It returns the current pin."""
        return self.pin
 
    def __str__(self):
        """It returns the string rep."""
        result =  'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result
