import sys


file = sys.argv[1]

fileobj = open(file, "r+")

text = fileobj.readlines()

for line in text:
	listLine = line.split()

	for i in range(len(listLine)):
		if listLine[i] == "to":
			listLine[i] = ""
	newLine = " ".join(listLine)
	fileobj.write(newLine+'\n')

fileobj.close()
