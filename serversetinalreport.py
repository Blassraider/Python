"""
This script processes the server log data to generate a user activity report.
"""
import os

def read_log_file(filename):
    """Reads file and returns a list of tuples containing log data."""
    data_list = []
    admin_fail = False
    
    with open(filename, 'r') as file:
        for line in file:
            parts = tuple(line.strip().split(','))
            if len(parts) == 4:
                data_list.append(parts)
                if parts[1].lower() == 'admin' and parts[3].lower() == 'failed':
                    admin_fail = True
                    
    return data_list, admin_fail

def calculate_stats(log_entries):
    """Processes the list of tuples and returns a dictionary of user counts."""
    user_counts = {}
    for entry in log_entries:
        user = entry[1]
        user_counts[user] = user_counts.get(user, 0) + 1
    return user_counts

def save_report(stats, output_file):
    """Writes the formatted statistics dictionary to a text file."""
    with open(output_file, 'w') as out_file:
        out_file.write("SERVER ACTIVITY SUMMARY\n")
        out_file.write("========================\n")
        for user, count in stats.items():
            out_file.write(f"User: {user} | Actions: {count}\n")

def main():
    """Mainline logic for the Server Sentinel Report."""
    input_fn = input("Enter the server log filename: ").strip()
    if not os.path.exists(input_fn):
        print("File error: Check the filename and try again.")
        return

    logs, has_admin_error = read_log_file(input_fn)
    user_stats = calculate_stats(logs)

    print(f"Processed {len(logs)} entries.")
    if has_admin_error:
        print("Warning: Admin failures detected!")

    default_name = "server_sentinel_summary_asgn5.txt"
    output_fn = input(f"Enter the filename to save the summary (or press Enter to use default): ").strip()
    final_output_name = output_fn if output_fn else default_name
    
    save_report(user_stats, final_output_name)
    print(f"Summary successfully saved to {final_output_name}")

if __name__ == "__main__":
    main()
