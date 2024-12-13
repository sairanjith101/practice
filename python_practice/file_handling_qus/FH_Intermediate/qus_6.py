# Write a program that reads a file and prints only lines containing a specific word.

with open('oldfile.txt', 'r') as file1:

    for line in file1:
        if 'python' in line.lower():
            print(line, end='')