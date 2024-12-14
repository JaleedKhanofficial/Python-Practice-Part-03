# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Prompt for the file name
    
file_name = input("Enter file name: ")

# Try to open the file and handle possible errors
try:
    file_handle = open(file_name, 'r')
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()

# Initialize count and total to compute the average
count = 0
total = 0.0

# Read through each line in the file
for line in file_handle:
    # Look for lines that start with 'X-DSPAM-Confidence:'
    if line.startswith('X-DSPAM-Confidence:'):
        # Find the position of the floating-point number and extract it
        space_pos = line.find('0')
        value = float(line[space_pos:].strip())
        
        # Add the value to total and increment the count
        total += value
        count += 1

# If we found any valid lines, compute and print the average
if count > 0:
    average = total / count
    print(f'Average spam confidence: {average}')
else:
    print("No X-DSPAM-Confidence lines found.")
