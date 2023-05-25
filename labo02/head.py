import sys

# Iterate over the command line arguments
for filename in sys.argv[1:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()

        # Print the first 10 lines
        for line in lines[:10]:
            print(line, end='')

# Extra

import sys

# Get the number of lines from the first command line argument
num_lines = int(sys.argv[1])

# Iterate over the remaining command line arguments
for filename in sys.argv[2:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()

        # Print the specified number of lines
        for line in lines[:num_lines]:
            print(line, end='')
