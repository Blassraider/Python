"""
File: bank_file_test.py
Tests the pickle load/dump functionality for the updated Bank class.
"""
from bank_file import Bank
from savingsaccount_JS import SavingsAccount
from checkingaccount_JS import CheckingAccount
import os
 
# complete the main function to test the save/load functionality of the Bank class.
def main():
    """
        # 1. Setup: Create a bank and add different account types
        # 2. Test Saving (Dump)
        # 3. Test Loading (Load)
        # 4. Verification (compare original and loaded bank states)
    """
    test_file = "bank_data.dat"
 
    # 1. Setup: Create a bank and add different account types
    print("=== 1. Setup: Create bank and add accounts ===")
    bank = Bank()
    bank.add(SavingsAccount("John", "1001", 1000.0))
    bank.add(CheckingAccount("John", "1001", 500.0))
    bank.add(SavingsAccount("Amy", "1002", 2000.0))
    bank.add(CheckingAccount("Amy", "1002", 300.0))
    print(bank)
 
    # 2. Test Saving (Dump)
    print("=== 2. Test Saving (Dump) ===")
    bank.save(test_file)
    print("Saved to", test_file)
    print("File exists:", os.path.exists(test_file))
 
    # 3. Test Loading (Load)
    print("\n=== 3. Test Loading (Load) ===")
    loadedBank = Bank(test_file)
    print(loadedBank)
 
    # 4. Verification (compare original and loaded bank states)
    print("=== 4. Verification ===")
    print("Original keys:", bank.getKeys())
    print("Loaded keys:  ", loadedBank.getKeys())
    print("Keys match:", bank.getKeys() == loadedBank.getKeys())
    johnSavings = loadedBank.get("John", "1001", "SavingsAccount")
    print("John's Savings balance:", johnSavings.getBalance())
    amyChecking = loadedBank.get("Amy", "1002", "CheckingAccount")
    print("Amy's Checking balance:", amyChecking.getBalance())
 
if __name__ == "__main__":
    main()
