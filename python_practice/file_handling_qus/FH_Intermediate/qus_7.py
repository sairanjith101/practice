# Create a program that reads a file and removes all empty lines.

with open('oldfile.txt', 'r') as file1:
    with open('check.txt', 'w') as file2:
        lines = file1.readlines()
        for line in lines:
            if line.strip():
                file2.write(line)
        