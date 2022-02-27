"""
Requirement:
    Read space separated file.
    Product quantity from 3rd row.
    Replace E103 with E111.
    Write unique user name and ID to new file

In file Sample:
User ID Product Strore
Tony E101 pencil CA
Rony E102 pencil DA
Tom E103 flip-flop CA
Tom E103 hatcher DA
Young E105 mattress GR
Jack E107 gun BR
"""

# Read space separated file
in_file = open('/home/krishnap/workbench/testDir/storeFile.txt','r')
# with open('/home/krishnap/workbench/testDir/storeFile.txt','r') as in_file:
data = in_file.read()
in_file.close()
print(data)

# Product quantity from 3rd row.
# Replace E103 with E111.
# Write unique user name and ID to new file

