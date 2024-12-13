# Write a program to read the contents of a text file and print it.

with open('sample.txt', 'r') as file1:
    lines = file1.readlines()
    for line in lines:
        print(line, end='')