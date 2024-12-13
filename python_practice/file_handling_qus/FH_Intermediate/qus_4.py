# Write a program to reverse the contents of a file line by line.

with open('newfile.txt', 'r') as file1:
    with open('reversefile.txt', 'w') as file2:
        lines = file1.readlines()
        for line in lines:
            reverse_line = line[::-1]
            file2.writelines(reverse_line)
