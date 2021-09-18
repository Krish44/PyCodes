"""
File operation checks
"""
# -----------------------------------------------------------
# Read a file and print the lines which are present multiple times.
'''
lines_seen = set()
printed = set()
in_file = open("input.txt", "r")

for line in in_file:
    if (line in lines_seen) & (line not in printed):
        print(line)
        printed.add(line)

    lines_seen.add(line)

'''
# -----------------------------------------------------------
# -----------------------------------------------------------
# Read file content
'''
import os
print("CWD:", os.getcwd())
file = open("file.txt", "w")
for i in range(5):
    file.write(str(i))
file.close()

file = open("file.txt", "r")
lines = file.readlines()
print(lines)
'''
# -----------------------------------------------------------
# Write even and odd in separate files

eve_file = open("even_data.txt","w")
odd_file = open("odd_data.txt","w")

for i in range(100):
    if i % 2 == 0:
        eve_file.write(str(i) + "\n")
    else:
        odd_file.write(str(i) + "\n")

eve_file.close()
odd_file.close()

# -----------------------------------------------------------


# Read a file "input.txt" and print how many times each line is present
