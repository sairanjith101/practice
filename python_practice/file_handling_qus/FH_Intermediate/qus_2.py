# Create a program that reads a file and writes its content to another file.

with open('sample.txt', 'r') as file1:
    with open('newfile.txt', 'w') as file2:
        lines = file1.readlines()
        if lines:
            file2.writelines(lines)
        else:
            print("File does not exists")