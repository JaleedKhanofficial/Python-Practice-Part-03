myFile = open('file.txt')
for line in myFile:
    line = line.rstrip()
    if not line.startswith('Lorem:'):
        continue
    print(line)