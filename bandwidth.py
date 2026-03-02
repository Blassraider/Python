import random
NORMAL_STATUS = "Normal"
HIGH_USAGE_STATUS = "High Usage!"
def main():
    try:
        hours_to_monitor = int(input("Monitoring duration (hours): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    total_bandwidth = 0.0
    highest_bandwidth = 0.0
    hours_above_80 = 0
    print(f"=== NETWORK BANDWIDTH MONITOR ===")
    print(f"\nStarting monitoring for {hours_to_monitor} hours")
    print(f"{'Hour':<6} {'Bandwidth Usage %':<20} {'Status':<15}")
    print("-" * 45)
    for hour in range(1, hours_to_monitor + 1):
        usage = round(random.uniform(1, 100), 1)
        status = NORMAL_STATUS
        if usage > 80:
            status = HIGH_USAGE_STATUS
            hours_above_80 += 1
        if usage > highest_bandwidth:
            highest_bandwidth = usage
        total_bandwidth += usage
        print(f"{hour:<6} {usage:<20} {status:<15}")
    average_bandwidth = total_bandwidth / hours_to_monitor if hours_to_monitor > 0 else 0
    print("\n" + "="*45)
    print("MONITORING SUMMARY")
    print("="*45)
    print(f"Monitoring period: {hours_to_monitor} hours")
    print(f"Highest bandwidth: {highest_bandwidth}%")
    print(f"Hours abouve 80%: {hours_above_80} hours")
    print(f"Hours above 80%: {hours_above_80} hours")
    print(f"Average bandwidth: {average_bandwidth:.1f}%")
if __name__ == "__main__":
    main()

        
