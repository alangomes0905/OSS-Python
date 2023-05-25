
import sys

# Initialize counters for lines, words, and characters
total_lines = 0
total_words = 0
total_chars = 0

# Iterate over the command line arguments
for filename in sys.argv[1:]:
    # Open the file in read-only mode
    with open(filename, 'r') as file:
        # Read the file content
        content = file.read()

        # Count the number of lines, words, and characters
        num_lines = len(content.split('\n'))
        num_words = len(content.split())
        num_chars = len(content)

        # Print the counts for the current file
        print(f"{num_lines}\t{num_words}\t{num_chars}\t{filename}")

        # Update the totals
        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

# Print the totals
print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")
