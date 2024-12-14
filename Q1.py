# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# Prompt for the file name
file_name = input("Enter file name: ")

# Try to open the file and handle possible errors
try:
    file_handle = open(file_name, 'r')
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()

# Initialize an empty list to store unique words
word_list = []

# Read through each line in the file
for line in file_handle:
    # Split the line into words
    words = line.split()
    # Process each word
    for word in words:
        # Check if the word is already in the list
        if word not in word_list:
            word_list.append(word)

# Sort the list of words in alphabetical order
word_list.sort()

# Print the sorted list of words
print(word_list)
