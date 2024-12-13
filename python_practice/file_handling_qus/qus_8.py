# Write a program to count the number of lines in a file.

# Initialize a counter for lines
line_count = 0

# Open the file in read mode
with open('newfile.txt', 'r') as file1:
    for line in file1:
        line_count += 1  # Increment the line count

print(f"The number of lines in the file is: {line_count}")
