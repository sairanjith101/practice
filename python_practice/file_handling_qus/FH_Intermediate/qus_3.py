# Implement a program to remove duplicate lines from a file.

# Open the file in read mode
with open('newfile.txt', 'r') as file:
    lines = file.readlines()  # Read all lines from the file

# Create a list to store unique lines while preserving the order
unique_lines = []
seen_lines = set()

# Loop through each line in the file
for line in lines:
    if line not in seen_lines:  # Check if the line is already seen
        unique_lines.append(line)  # Add the line to the list
        seen_lines.add(line)  # Add the line to the set

# Open the file in write mode to overwrite it with unique lines
with open('newfile.txt', 'w') as file:
    file.writelines(unique_lines)

print("Duplicate lines have been removed.")

