from bankaccount import BankAccount
 
class SavingsAccount(BankAccount):
    """This class represents a savings account
    with the owner's name, PIN, and balance."""
 
    RATE = 0.02    
 
    def __init__(self, name, pin, balance = 0.0):
        BankAccount.__init__(self, name, pin, balance)
 
    def computeInterest(self):
        """This computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
 
    def __str__(self):
        """This returns the string rep with account type."""
        result =  'Account: Savings\n'
        result += 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result
 
