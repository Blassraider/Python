"""
This script reads the server names from a file and identifies their type.
"""

def get_server_names(filename):
    """Reads the server names from a file and returns them as a list."""
    names = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                name = line.strip()
                if name:
                    names.append(name)
    except FileNotFoundError:
        return None
    return names

def identify_server_type(server_name):
    """Identifies the server type based on the name suffix."""
    if server_name.endswith("-prod"):
        return "Production"
    elif server_name.endswith("-dev") or server_name.endswith("-lab"):
        return "Development"
    else:
        return "Unknown"

def print_report(server_names):
    """Generates and prints the formatted Server Inventory Report."""
    print("--- SERVER INVENTORY REPORT ---")
    for name in server_names:
        server_type = identify_server_type(name)
        print(f"Server: {name:<15} | Type: {server_type}")
    print("-" * 31)

def main():
    """Mainline logic for the server identification report."""
    filename = input("Enter the filename containing server names: ")
    
    servers = get_server_names(filename)
    
    if servers is None:
        print("Error: The file could not be found.")
    elif len(servers) == 0:
        print("The file is empty.")
    else:
        print_report(servers)

if __name__ == "__main__":
    main()
