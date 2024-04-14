import re

# Read the contents of the file 'new.txt'
with open('new.txt', 'r') as file:
    lines = file.readlines()

# Define a regular expression pattern to match IP addresses
ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Filter the lines and keep only the ones that match the IP address pattern
ip_addresses = [line.strip() for line in lines if re.match(ip_pattern, line)]

# Write the IP addresses to a new file 'new.csv'
with open('new.csv', 'w') as file:
    for ip_address in ip_addresses:
        file.write(ip_address + '\n')

print(f"Exported {len(ip_addresses)} IP addresses to 'new.csv'.")

