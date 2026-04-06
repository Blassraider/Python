"""
Author: Jaylen Stingley
Purpose: GUI version of the disk usage calculator using breezypythongui.
         Reports disk usage in KB, MB, and GB and performs a quota analysis.
"""
 
from breezypythongui import EasyFrame
 
QUOTA_GB = 50
CONVERSION_FACTOR = 1024
 
 
class DiskUsageCalculator(EasyFrame):
    """Calculates and reports disk usage and quota analysis."""
 
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Disk Usage Calculator", width=400, height=300)
 
        self.addLabel(text="Disk Usage (KB):", row=0, column=0)
        self.inputField = self.addFloatField(value=0.0, row=0, column=1, width=14)
 
        self.addButton(text="Calculate", row=1, column=0, command=self.calculate)
        self.addButton(text="Reset",     row=1, column=1, command=self.reset)
 
        self.addLabel(text="-- Disk Usage Report --", row=2, column=0, columnspan=2)
 
        self.addLabel(text="Kilobytes (KB):", row=3, column=0)
        self.kbField = self.addIntegerField(value=0, row=3, column=1,
                                            width=14, state="readonly")
 
        self.addLabel(text="Megabytes (MB):", row=4, column=0)
        self.mbField = self.addFloatField(value=0.0, row=4, column=1,
                                          width=14, precision=2, state="readonly")
 
        self.addLabel(text="Gigabytes (GB):", row=5, column=0)
        self.gbField = self.addFloatField(value=0.0, row=5, column=1,
                                          width=14, precision=2, state="readonly")
 
        # ── Quota Analysis labels & output fields ──────────────
        self.addLabel(text="-- Quota Analysis --", row=6, column=0, columnspan=2)
 
        self.addLabel(text="Quota: " + str(QUOTA_GB) + " GB", row=7, column=0, columnspan=2)
 
        self.addLabel(text="Used (GB):", row=8, column=0)
        self.usedField = self.addFloatField(value=0.0, row=8, column=1,
                                            width=14, precision=2, state="readonly")
 
        self.addLabel(text="Remaining (GB):", row=9, column=0)
        self.remainField = self.addFloatField(value=0.0, row=9, column=1,
                                              width=14, precision=2, state="readonly")
 
        self.addLabel(text="Percentage Used:", row=10, column=0)
        self.percentField = self.addFloatField(value=0.0, row=10, column=1,
                                               width=14, precision=1, state="readonly")
 
    def calculate(self):
        """Reads KB input, computes conversions and quota analysis, displays results."""
        usage_kb = self.inputField.getNumber()
 
        usage_mb     = usage_kb / CONVERSION_FACTOR
        usage_gb     = usage_mb / CONVERSION_FACTOR
        remaining_gb = QUOTA_GB - usage_gb
        percentage   = (usage_gb / QUOTA_GB) * 100
 
        self.kbField.setNumber(int(usage_kb))
        self.mbField.setNumber(usage_mb)
        self.gbField.setNumber(usage_gb)
        self.usedField.setNumber(usage_gb)
        self.remainField.setNumber(remaining_gb)
        self.percentField.setNumber(percentage)
 
    def reset(self):
        """Resets all fields to their default values."""
        self.inputField.setNumber(0.0)
        self.kbField.setNumber(0)
        self.mbField.setNumber(0.0)
        self.gbField.setNumber(0.0)
        self.usedField.setNumber(0.0)
        self.remainField.setNumber(0.0)
        self.percentField.setNumber(0.0)
 
 
def main():
    DiskUsageCalculator().mainloop()
 
 
if __name__ == "__main__":
    main()
