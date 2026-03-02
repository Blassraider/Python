import os

def main():
    # Defining the constants
    INPUT_FILE = "raw_input.txt"
    OUTPUT_FILE = "output_report.txt"
    THRESHOLD = 500

    # Use the os module to make sure the file is accessible
    if not os.path.exists(INPUT_FILE):
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print(f"Current working directory: {os.getcwd()}")
        return


    try:
        # Use with-open statements for File I/O
        with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w') as outfile:
            
            # Write the header to the report
            outfile.write("--- SYSTEM QUOTA REPORT ---\n")
            
            # Process each line in the input file
            for line in infile:
                # Strip whitespace and split by colon
                line = line.strip()
                if not line:
                    continue 
                
                username, usage_str = line.split(":")
                usage_mb = int(usage_str)
                
                # Determine the status based on the 500MB threshold
                status = "OVER LIMIT" if usage_mb > THRESHOLD else "OK"
                
                # Outputis formating report by using f-strings
                # Convert the numbers back to strings implicitly to f-string
                report_line = f"User: {username:<10} | Usage: {usage_mb} MB | Status: {status}\n"
                outfile.write(report_line)
        
        print(f"Success! Report generated in '{OUTPUT_FILE}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
