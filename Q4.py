# # Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# Prompt for the file name
file_name = input("Enter file name: ")

# Try to open the file and handle possible errors
try:
    file_handle = open(file_name, 'r')
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()

# Initialize a counter for the lines that start with 'From '
count = 0

# Read through each line in the file
for line in file_handle:
    # Only process lines that start with 'From '
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Print the second word (email address)
        print(words[1])
        # Increment the counter
        count += 1

# Print the count of lines starting with 'From '
print(f"There were {count} lines in the file with From as the first word.")
