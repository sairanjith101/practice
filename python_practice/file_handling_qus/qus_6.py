# Write a program to read a file line by line and print each line.

with open('sample3.txt', 'r+') as file1:
    for line in file1:
        print(line, end='')