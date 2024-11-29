# open the file for reading
with open("sampleFile.txt", "r") as f:
    # read the lines into a list
    lines = f.readlines()

# sort the lines in ascending order
lines.sort()

# open the file for writing
with open("sortedFile.txt", "w") as f:
    # write the sorted lines to the file
    f.writelines(lines)
