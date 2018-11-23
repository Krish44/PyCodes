  i = 44044044
print("Value of i: ", i)
print("Address of i: ", id(i))
k = [3,4,5,6,7]
j = [1,"Linux",3,"bash",[1,2,"sh"],7,8,9]
print(j)
print("Accessing multi dimension j[4][2]:", j[4][2])
print("Index [1]:", j[1])
print("Index [-4]:", j[-4])
j.pop()
print("After pop Index [-1]:", j[-1])
print("j list after pop:", j)
j.extend(k)
print("j list after extending:", j)
print("Min of k:", min(k))
print(i)
print("Length of list k:", len(k))

a = "ab_"
print("a:", a)
print("Multiply a:",a*2)

# Dictionary:
a = {'IN': 'India', 'US': 'United States of America', 'ES': 'Espanol'}
print("Dictionary a:", a)
print("keys: ", a.keys())
print("Values: ", a.values())
# Convert dict value to  list
C_list = list(a.values())
# Print list with comma and space separated representation
print("List:", C_list, "\nLength of list:", len(C_list), "\nJust list:", ('| '.join(C_list)))
# (', '.join(C_list)) is equivalent to tr command in Linux
sep_list = ' '.join(C_list)
print("Separated list:", sep_list)
for country in C_list:
    print("Country:", country)
