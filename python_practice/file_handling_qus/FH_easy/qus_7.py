# Create a program that appends text to an existing file.

line = "\nselam"

with open('newfile.txt', 'a') as file1:
    file1.write(line)