from bank import Bank
from savingsaccount_JS import SavingsAccount
from checkingaccount_JS import CheckingAccount
 
def main():
    """
    # 1. Add different account types for the same person
    # 2. Test Polymorphic Interest - Only the SavingsAccount should be affected
    # 3. Test Retrieval
    # 4. Show final state
    """
    bank = Bank()
 
    # 1. Add different account types for the same person
    bank.add(SavingsAccount("Jaylen", "2222", 1000.0))
    bank.add(CheckingAccount("Jaylen", "2222", 500.0))
    print("=== Initial State ===")
    print(bank)
 
    # 2. Test Polymorphic Interest - Only the SavingsAccount should be affected
    totalInterest = bank.computeInterest()
    print("=== After computeInterest() ===")
    print("Total interest earned:", totalInterest)
    print(bank)
 
    # 3. Test Retrieval
    print("=== Test Retrieval ===")
    account = bank.get("Jaylen", "2222", "SavingsAccount")
    print("Retrieved Jaylen's Savings:", account)
    account = bank.get("Jaylen", "2222", "CheckingAccount")
    print("Retrieved Jaylen's Checking:", account)
    account = bank.get("Jaylen", "2222", "SavingsAccount")
    account.deposit(500.0)
    print("After depositing $500 to Jaylen's Savings:")
    print(account)
 
    # 4. Show final state
    print("=== Final State ===")
    print(bank)
 
if __name__ == "__main__":
    main()
