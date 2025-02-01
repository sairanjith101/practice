with open('samplefile.txt', 'r') as file1:
    with open('newfile.txt', 'w') as file2:
        # lines = file1.readlines()
        for line in file1.readlines():
            if 'melon' in line.lower():
                file2.writelines(line)