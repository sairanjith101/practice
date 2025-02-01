with open('samplefile.txt', 'r') as file1:
    with open('newfile.txt', 'w') as file2:
        lines = sorted(file1)
        if lines:
            file2.writelines(lines)