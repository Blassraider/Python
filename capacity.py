import random
STATUS_HEALTHY = "Healthy"
STATUS_WARNING = "WARNING (75%+)"
STATUS_CRITICAL = "CRITICAL (90%+)"
def main():
    current_storage = float(input("Enter current storage used (TB): "))
    server_limit = float(input("Enter server capacity limit (TB): "))
    expected_growth_pct = float(input("Enter expected monthly growth (%): "))
    month = 0
    print(f"\n{'Month':<8} {'Storage (TB)':<18} {'Status':<15}")
    print("-" * 45)
    while current_storage < server_limit:
        month += 1
        volatility = random.uniform(-0.02, 0.05)
        actual_growth_rate = (expected_growth_pct / 100) + volatility
        current_storage += current_storage * actual_growth_rate
        usage_pct = current_storage / server_limit
        if usage_pct >= 0.90:
            status = STATUS_CRITICAL
        elif usage_pct >= 0.75:
            status = STATUS_WARNING
        else:
            status = STATUS_HEALTHY
        print(f"{month:<8} {current_storage:<18.2f} {status:<15}")
    print("-" * 45)
    print(f"CRITICAL: Server will reach capacity in {month} months.")
if __name__ == "__main__":
    main()
            
    
