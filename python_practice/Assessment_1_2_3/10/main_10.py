with open('sampleFile.txt', 'r') as input_file:
    with open('outputFile.txt', 'w') as output_file:
        for line in input_file:
            if 'melon' in line.lower():
                output_file.write(line)
