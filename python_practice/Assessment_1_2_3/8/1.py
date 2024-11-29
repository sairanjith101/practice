with open('testFile.txt', 'r') as f:
    lines = f.readlines()

lines.sort()

with open("sortedFile.txt", 'w') as f:
    f.writelines(lines)