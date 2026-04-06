"""
Author: Jaylen Stingley
Purpose: GUI tax calculator using breezypythongui.
         Computes federal income tax at a 20% flat rate with a
         $10,000 standard deduction plus $3,000 per dependent.
"""
 
from breezypythongui import EasyFrame
 

TAX_RATE            = 0.20
STANDARD_DEDUCTION  = 10000.0
DEPENDENT_DEDUCTION = 3000.0
 
 
class TaxCalculator(EasyFrame):
    """Calculates income tax with standard and dependent deductions."""
 
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Tax Calculator", width=420, height=280)
 
        
        self.addLabel(text="Gross Income ($):", row=0, column=0)
        self.grossField = self.addFloatField(value=0.0, row=0, column=1,
                                             width=14, precision=2)
 
        self.addLabel(text="Number of Dependents:", row=1, column=0)
        self.dependentsField = self.addIntegerField(value=0, row=1, column=1, width=14)
 
        
        self.addButton(text="Compute", row=2, column=0,
                       columnspan=2, command=self.compute)
 
        
        self.addLabel(text="-- Tax Breakdown --", row=3, column=0, columnspan=2)
 
        self.addLabel(text="Standard Deduction ($):", row=4, column=0)
        self.stdField = self.addFloatField(value=0.0, row=4, column=1,
                                           width=14, precision=2, state="readonly")
 
        self.addLabel(text="Dependent Deduction ($):", row=5, column=0)
        self.depField = self.addFloatField(value=0.0, row=5, column=1,
                                           width=14, precision=2, state="readonly")
 
        self.addLabel(text="Taxable Income ($):", row=6, column=0)
        self.taxableField = self.addFloatField(value=0.0, row=6, column=1,
                                               width=14, precision=2, state="readonly")
 
        self.addLabel(text="Income Tax ($):", row=7, column=0)
        self.taxField = self.addFloatField(value=0.0, row=7, column=1,
                                           width=14, precision=2, state="readonly")
 
        self.addLabel(text="Net Income ($):", row=8, column=0)
        self.netField = self.addFloatField(value=0.0, row=8, column=1,
                                           width=14, precision=2, state="readonly")
 
    def compute(self):
        """Reads inputs, computes tax, and displays the breakdown."""
        gross_income   = self.grossField.getNumber()
        num_dependents = self.dependentsField.getNumber()
 
        dep_deduction   = DEPENDENT_DEDUCTION * num_dependents
        total_deduction = STANDARD_DEDUCTION + dep_deduction
        taxable_income  = max(0.0, gross_income - total_deduction)
        income_tax      = taxable_income * TAX_RATE
        net_income      = gross_income - income_tax
 
        self.stdField.setNumber(STANDARD_DEDUCTION)
        self.depField.setNumber(dep_deduction)
        self.taxableField.setNumber(taxable_income)
        self.taxField.setNumber(income_tax)
        self.netField.setNumber(net_income)
 
 
def main():
    TaxCalculator().mainloop()
 
 
if __name__ == "__main__":
    main()
 
