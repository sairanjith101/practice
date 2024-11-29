# both the reading and writing of file
with open('sampleFile.txt','rb') as file1, open('newFile.txt','wb') as file2:
	while True:
		byte = file1.read(1)
		if byte:
			file2.write(byte)
		else: break