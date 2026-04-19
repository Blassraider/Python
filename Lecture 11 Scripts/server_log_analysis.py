"""
server_log_analysis.py
Reads server_log.csv, strips comments, cleans NaN values,
calculates mean response times, and visualizes with a pie chart.
"""
import pandas as pd
import matplotlib.pyplot as plt
 
frame = pd.read_csv("server_log.csv", comment="#")
 
print("=== Raw Data ===")
print(frame.to_string())
print()
 
service_cols = ["Login_API", "Database_Query", "File_Upload", "Auth_Service"]
 
for col in service_cols:
    col_mean = frame[col].mean()
    frame[col] = frame[col].fillna(col_mean)
    print(f"  {col} mean (used to fill NaN): {round(col_mean, 2)} ms")
 
print()
print("=== Cleaned Data ===")
print(frame.to_string())
print()
 
means = {col: round(frame[col].mean(), 2) for col in service_cols}
 
print("=== Mean Response Times ===")
for service, avg in means.items():
    print(f"  {service}: {avg} ms")
 
labels = list(means.keys())
slices = list(means.values())
 
plt.figure(figsize=(7, 7))
plt.pie(slices, labels=labels, autopct="%1.1f%%")
plt.title("Average Server Response Times by Service")
plt.savefig("server_response_chart.png", dpi=150)
print("Chart saved to server_response_chart.png")
