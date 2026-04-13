from bankaccount import BankAccount
 
class CheckingAccount(BankAccount):
    """This class represents a checking account
    with the owner's name, PIN, and balance."""
 
    def __init__(self, name, pin, balance = 0.0):
        BankAccount.__init__(self, name, pin, balance)
 
    def __str__(self):
        """This returns the string rep with account type."""
        result =  'Account: Checking\n'
        result += 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result
