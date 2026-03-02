"""
Author: Jaylen Stingley
Purpose: This program calculates and reports disk usage in KB, MB and GB based on user input and performs a qouta analysis
"""
QUOTA_GB = 50
CONVERSION_FACTOR = 1024
kb_string = input("Enter disk usage in Kilobytes (KB): ")
usage_kb = float(kb_string)
usage_mb = usage_kb / CONVERSION_FACTOR
usage_gb = usage_mb / CONVERSION_FACTOR
remaining_gb = QUOTA_GB - usage_gb
percentage_used = (usage_gb / QUOTA_GB) * 100
print("Disk Usage Report for User:")
print("=" * 28)
print("Usage in Kilobytes (KB):", int(usage_kb))
print("usage in Megabytes (MB):", round(usage_mb, 2))
print("Usage in Gigabytes (GB):", round(usage_gb, 2))
print()
print("Quota Analysis:")
print("-" * 28)
print("Quota:", QUOTA_GB, "GB")
print("Used:", round(usage_gb, 2), "GB")
print("Remaining:", round(remaining_gb, 2), "GB")
print("Percentage used: " + str(round(percentage_used, 1)) + "%")

