with open('sample.txt', 'r') as file1:
    lines = file1.readlines()

lines.sort()

with open('stored.txt', 'w') as file2:
    file2.writelines(lines)