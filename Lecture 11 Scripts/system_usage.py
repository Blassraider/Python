import random
import math
import matplotlib.pyplot as plt
 
random.seed(42)
cpu_usage = [round(random.uniform(20, 95), 1) for _ in range(8)]
hours = list(range(1, 9))
 
# The Statistical functions
def mean(lyst):
    if len(lyst) == 0:
        raise ValueError("List must be non-empty. ")
    return sum(lyst) / len(lyst)
 
def median(lyst):
    if not lyst: # Empties list returns false
        raise ValueError("List must be non-empty. ")
    copy = sorted(lyst) # Constructs a copy of sorted lyst
    n = len(copy)
    midpoint = n // 2
    if n % 2 == 1:
        return copy[midpoint]
    else:
        return mean([copy[midpoint - 1], copy[midpoint]])
 
def std(lyst):
    if len(lyst) == 0:
        raise ValueError("List must be non-empty. ")
    average = mean(lyst)
    differences = map(lambda x: x - average, lyst)
    squares = list(map(lambda x: x ** 2, differences))
    return math.sqrt(mean(squares))

print("Max:", max(cpu_usage))
print("Min:", min(cpu_usage))
print("Mean:", round(mean(cpu_usage), 2))
print("Median:", round(median(cpu_usage), 2))
print("Std Dev:", round(std(cpu_usage), 2))

plt.figure(figsize=(6, 4))
plt.bar(hours, cpu_usage, width=0.5, color='skyblue')
plt.title("CPU Usage Over 8-Hour Shift")
plt.xlabel("Hour")
plt.ylabel("CPU Usage (%)")
plt.xticks(hours)
plt.show()
 

 

