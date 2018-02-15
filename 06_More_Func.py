"""
Code details about use of modules, their format, Doc string representation
Date-Time 
"""
import os
import glob2
import datetime
import time
"""
Doc String will be written inside 3ple quotes.
Order of call: module.class.method()
"""
print("Print OS doc string: ", os.__doc__)
# When a lib is called, init.py will be executed for that lib
print("Package location: ", os.__file__)
OldPath = os.getcwd()
print("Initial Dir: ", OldPath)
os.chdir("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder")
NewPath = os.getcwd()
print("Changed Dir: ", NewPath)
FileList = os.listdir(NewPath)
print("File list using 'OS' listing: ", FileList)
GlobList = glob2.glob("*.txt")  # Helpful to select a specific type of file
print("List of files using 'glob' method:", GlobList)

# Utilization of datetime objects
date1 = datetime.datetime.now()  # Based on computer timing
print("Present timestamp: ", date1)
date2 = date1.strftime("%Y_%M_%d-%H-%M-%S")  # .strftime for formatting date-time
print("Formatted Date: ", date2)
After1 = date1+datetime.timedelta(days=2)
print("Altered timestamp: ", After1)

# Use of time module
lst = []  # Later add time at 3 diff sec to this list
for i in range(3):
    lst.append(datetime.datetime.now())
    time.sleep(1)
for i in lst:
    print(i)

# create a script that merges the three text files into a new text file containing the text of all three files
# FileList = glob2.glob("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\*.txt")
os.chdir("C:\Drives_kp\Learning\PyCodes\PracticeFiles\TestFolder\MergeFiles")
FileList = glob2.glob("*.txt")
NewFile1 = datetime.datetime.now()
NewFile1 = NewFile1.strftime("%Y-%m-%d-%H-%M")+".txt"
with open(NewFile1, 'a+') as MergFile:
    for FilNames in FileList:
        with open(FilNames, 'r') as FL1:
            data = FL1.read()
            MergFile.write(data+"\n")
    MergFile.seek(0)  # Reposition pointer before reading
    print("Merged file content: \n", MergFile.read())
