# How do you copy contents from one file to another only if the source file is not empty using Python?

with open('sample2.txt', 'r') as file1:
    with open('newfile.txt', 'w') as file2:
        lines = file1.readlines()
        if lines:
            file2.writelines(lines)