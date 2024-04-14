import csv

# Read the input file
with open('unclean.csv', 'r') as file:
    reader = csv.reader(file)
    ip_addresses = []
    for row in reader:
        try:
            ip_addresses.append(row[0])
        except IndexError:
            # Skip the row if it doesn't have an IP address
            continue

# Remove duplicate IP addresses
unique_ips = list(set(ip_addresses))

# Write the unique IP addresses to the output file
with open('clean.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for ip in unique_ips:
        writer.writerow([ip])

print("Duplicate IP addresses removed. Results exported to 'clean.csv'.")
