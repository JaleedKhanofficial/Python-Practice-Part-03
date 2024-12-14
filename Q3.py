myFile = input("Enter the file name: ") #file is file.txt

try: 
    fhand = open(myFile)
except:
    print(f"File cannot be opened:{myFile}")
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Lorem:'):
        count = count+1
        # continue
print(f"There were {count} subject line in {myFile}")
