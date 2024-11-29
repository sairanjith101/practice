FileName = ("sampleFile.txt")
data=open(FileName).readlines()
data.sort()
for i in range(len(data)):
    print("\n", data[i])
