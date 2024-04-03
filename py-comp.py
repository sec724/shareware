# Function to read a file and return a set of lines
def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.read().splitlines())

# Main function to compare two files and export unique lines to a new file
def compare_and_export(main_file, new_file, output_file):
    main_lines = read_file(main_file)
    new_lines = read_file(new_file)

    # Lines in new.txt that are not in main.csv
    unique_lines = new_lines - main_lines

    # Export unique lines to a new file
    with open(output_file, 'w') as file:
        for line in unique_lines:
            file.write(line + '\n')

# File paths
main_file = 'main.csv'
new_file = 'new.txt'
output_file = 'unique.csv'

# Compare files and export unique lines
compare_and_export(main_file, new_file, output_file)

print("Unique lines exported to 'unique.csv'")
