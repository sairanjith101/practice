with open('sample.txt', 'r') as file1:
    with open('new.txt', 'w') as file2:
        read_line = file1.readlines()
        read_line.sort()
        if read_line:
            file2.writelines(read_line)