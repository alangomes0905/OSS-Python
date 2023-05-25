import sys

# Iterate over the command line arguments
for filename in sys.argv[1:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read and print the file content
        content = file.read()
        print(content)

    # Close the file automatically after reading and printing the content


import sys

# Initialize line number
line_number = 1

# Iterate over the command line arguments
for filename in sys.argv[1:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()

        # Print the content with line numbers
        for line in lines:
            # Format the line number to be 6 characters wide
            line_number_formatted = str(line_number).rjust(6)

            # Print the line number, tab character, and line content
            print(line_number_formatted, line, end='')

            # Increment the line number
            line_number += 1

    # Print an empty line between files
    print()
