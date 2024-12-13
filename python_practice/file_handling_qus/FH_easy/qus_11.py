# Write a program that reads and prints the last line of a file.

with open('newfile.txt', 'r') as file1:
    lines = file1.readlines()
    if lines:
        print(lines[-1].strip())
    else:
        print("File is Empty")