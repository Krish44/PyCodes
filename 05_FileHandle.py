# Code reads a file and prints out its contents
# Date : 15 -12 -2017 Last edited

f1 = open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\TextFile.txt", 'r')
print(type(f1))
print("Reading file content on screen:\n", f1.read())
f1.seek(0)  # Places pointer back at the zero position of the text file
content = f1.readlines()
print("File read as it is in a List: ", content)
content2 = [i.rstrip("\n") for i in content]
print("Data after formatting: ", content2)
f1.close()

# Writing a file:
f2 = open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\\NewFile.txt", 'w')
f2.write("This one is a newfile")
f2.write("\nAdding another line")
MyList = ['Line A', 'Line B', "Line C"]  # Adding contents from a list
for item in MyList:
    f2.write("\n"+item)
f2.close()

# Appending to a file: (File will be created if does not exists)
f3 = open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\\NewFile.txt", 'a')
f3.write("\nAppended line")
f3.close()

# with - Cleaner code while handling files
with open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\\NewFile.txt", 'a+') as f4:
    f4.seek(0)
    data = f4.read()
    print("From section having 'with' statement :\n", data)
    f4.write("\nAdded using with statement")
    f4.seek(0)
    data = f4.read()
    print(data)

# Exercise:  print out converted temperature
temperatures = [10, -20, -289, 100]
with open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\\ExerFile.txt", 'w') as OutFile:
    for value in temperatures:
        if float(value) > -273.15:
            fh = value*9/5+32
            OutFile.write(str(fh)+"\n")
