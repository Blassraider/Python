
# The Module-Level Variable (Global Scope)
SERVERS = {
    "Web_Alpha": "Online",
    "DB_Storage": "Offline",
    "Mail_Relay": "Online"
}

def display_menu():
    """The Helper to show the UI."""
    print("\n" + "="*30)
    print("  SERVER MANAGEMENT CONSOLE")
    print("="*30)
    print("1. View All Server Statuses")
    print("2. Update a Server Status")
    print("3. Add a New Server")
    print("4. Exit")
    print("="*30)

def show_status():
    """Option 1: Displays the current state of all servers."""
    print("\n--- Current Server Status ---")
    for name, status in SERVERS.items():
        print(f" - {name}: [{status}]")

def update_server():
    """Option 2: Updates an existing server's status."""
    server_name = input("Enter server name: ")
    if server_name in SERVERS:
        status = input("Enter new status (Online/Offline): ")
        SERVERS[server_name] = status
        print(f"\n[Success] {server_name} is now {status}.")
    else:
        print(f"\n[Error] Server '{server_name}' not found.")

def add_server():
    """Option 3: Adds a new server to the global dictionary."""
    new_name = input("Enter the new server name: ")
    if new_name in SERVERS:
        print(f"\n[Error] Server '{new_name}' already exists.")
    else:
        SERVERS[new_name] = "Offline"
        print(f"\n[Success] Added {new_name} to the fleet.")

def main():
    """The 'Manager' function using a dispatch dictionary instead of elif."""
    
    # The map choices to function names (with no parenthesis)
    dispatch_table = {
        "1": show_status,
        "2": update_server,
        "3": add_server
    }
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        # Handle the exit condition first
        if choice == "4":
            print("Exiting management console. Goodbye!")
            break

        # Use the dictionary to find the function
        action = dispatch_table.get(choice)

        if action:
            action() # Execute the function found in the dictionary
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
