import re
import os
import sys
from datetime import datetime

# Function to filter log entries by date
def filter_logs_by_date(log_file_path, target_date, output_file_path):
    # Convert the target date to a datetime object for comparison
    target_date = datetime.strptime(target_date, "%Y-%m-%d")
    
    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # Open the log file and read it line by line
    with open(log_file_path, 'r') as log_file:
        matching_logs = []
        for line in log_file:
            # Use regex to match the timestamp pattern at the start of the log entry
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
            
            # If a timestamp is found, compare the date part
            if match:
                log_timestamp = match.group(1)
                log_date_obj = datetime.strptime(log_timestamp.split(' ')[0], "%Y-%m-%d")
                
                # If the log date matches the target date, add to the result
                if log_date_obj.date() == target_date.date():
                    matching_logs.append(line.strip())

        # Write the matching logs to the output file
        with open(output_file_path, 'w') as output_file:
            if matching_logs:
                output_file.write(f"Log entries for {target_date.date()}:\n")
                for log in matching_logs:
                    output_file.write(f"{log}\n")
            else:
                output_file.write(f"No log entries found for {target_date.date()}\n")

# Ensure the user has provided the target date
if len(sys.argv) < 2:
    print("Please provide the target date in the format YYYY-MM-DD.")
    sys.exit(1)

# Get the target date from the command line argument
target_date = sys.argv[1]

# Define the input log file path and output file path
log_file_path = 'tests_log.log'  # The log file name
output_file_path = r'C:\Users\PUSHKAR\OneDrive\Desktop\projects\tech-campus-recruitment-2025\output\output_YYYY-MM-DD.txt'  # Full output path

# Call the function to filter and store the logs
filter_logs_by_date(log_file_path, target_date, output_file_path)

print(f"Filtered logs have been written to {output_file_path}")
