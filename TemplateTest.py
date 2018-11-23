from string import Template
# open the file
filein = open('TemplateTest.txt')
# read it
src = Template(filein.read())
# document data
title = "This is the title"
subtitle = "And this is the subtitle"
list1 = ['first', 'second', 'third']
d = {'title': title, 'subtitle': subtitle, 'list': ('\n'.join(list1))}
# do the substitution
result = src.substitute(d)
print(result, "\n=========================")

# List Student stores the name and marks of three students
Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]
print("Index 2:", Student[2])
# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print("i[1]=", i[1])
    print(t.substitute(name=i[0], marks=i[1]))
