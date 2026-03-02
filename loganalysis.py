"""
Author: Jaylen Stingley
Purpose: This script calculates the total storage required for a specific number of log messages, providing exact, rounded-up, and rounded-down KB.
"""
import math
CONVERSION_FACTOR = 1024
log_message = input("Enter the log message: ")
num_messages = int(input("Enter the number of log messages: "))
message_length_bytes = len(log_message)
total_size_bytes = message_length_bytes * num_messages
exact_kb = total_size_bytes / CONVERSION_FACTOR
rounded_up_kb = math.ceil(exact_kb)
rounded_down_kb = math.floor(exact_kb)
print("=== LOG STORAGE CALCULATOR ===")
print()
print("Log message:", log_message)
print("Message length:", message_length_bytes, "characters")
print()
print("Storage for", num_messages, "messages:")
print("Exact kilobytes:", exact_kb)
print("Rounded UP (ceil):", str(rounded_up_kb), "KB")
print("Rounded DOWN (floor):", str(rounded_down_kb), "KB")


