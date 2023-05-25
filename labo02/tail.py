import sys

# Iterate over the command line arguments
for filename in sys.argv[1:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()

        # Select the last 10 lines
        last_10_lines = lines[-10:]

        # Print the last 10 lines
        for line in last_10_lines:
            print(line, end='')


#Extra

import sys

# Get the number of lines from the first command line argument
num_lines = int(sys.argv[1])

# Iterate over the remaining command line arguments
for filename in sys.argv[2:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()

        # Select the specified number of lines
        last_lines = lines[-num_lines:]

        # Print the specified number of lines
        for line in last_lines:
            print(line, end='')
