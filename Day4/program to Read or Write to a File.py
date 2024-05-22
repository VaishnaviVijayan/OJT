f = open("demofile2.txt", "a")
f.write("hehehehehehehe!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

