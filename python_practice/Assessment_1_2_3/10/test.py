with open('demo.txt', 'r') as file1:
    with open('new.txt', 'w') as file2:
        for line in file1:
            if 'melon' in line.lower():
                file2.write(line)