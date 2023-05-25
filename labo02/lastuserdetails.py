with open('/etc/passwd', 'r') as file:
    lines = file.readlines()

# Get the last line from the file
last_line = lines[-1]

# Split the line by ':' delimiter
user_details = last_line.split(':')

# Extract the required information
username = user_details[0]
userid = user_details[2]
home_directory = user_details[5]

# Print the extracted information
print("Last User Details:")
print("Username:", username)
print("User ID:", userid)
print("Home Directory:", home_directory)

