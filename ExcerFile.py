# Exercise tasks :
"""
# Includes concepts from
# list- Dictionary - set - map - filer - lambda
"""
# -----------------------------------------------------------
# Take the user's name and print
'''
Name = input("Enter the Title: ")
print("Title is :", Name)
'''
# -----------------------------------------------------------
# Take two numbers from the user and print their multiplication.
'''
num1, num2 = map(int, input("Enter the data \n(Space separated): \n").split())
# map function maps receiving data to integer
print("Type of data:", type(num1))
print("product =", (num1)*(num2))
'''
# -----------------------------------------------------------
# Find all the unique elements of a list.
#  Input; a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]. Output; [1, 2, 3, 4]
'''
lst1 = ['a', 'b', 'c', 'd']
lst2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]

sltr1 = list(lst1)
print("List:", sltr1)
print(type(sltr1))
print("List separation with string values: ", ' | '.join(sltr1))

sltr2 = map(str, lst2)
print("Mapped to string, list:",sltr2)
print("List separation with integer values: ", ' | '.join(sltr2))
# Need to map the element to string since join will consider only string values

uniq_lst2 = set(lst2)
print("Remove duplicates fro the list:", uniq_lst2)
print("formatted display:", ' | '.join(map(str, uniq_lst2)))
'''
# -----------------------------------------------------------
# Find the number of occurrences of every element in the list [1,2,1,2,1,2,3,4,1,2,3]
'''
d = [1, 2, 1, 2, 1, 2, 3, 4, 1, 2, 3]
print("Original List:", d)
#  d1 = d.sort()
print("sorted list:", sorted(d))  # d.sort will not return value directly
d2 = set(d)       # To be noted that the order of the list elements will be changed
ext_dict = {}
print("Uniq list:", d2)
for i in d2:
    print(i, "present", d.count(i), "times")
    # Load the data and count in a dictionary
    ext_dict[i] = d.count(i)

print(ext_dict)

# Try printing data from dictionary
for k in (ext_dict.keys()):
    print(k, "found", ext_dict[k], "times")
'''
# -----------------------------------------------------------
# To print vertical data in new line or any other representation.
'''
print('\n'.join(dir("dict")))
'''
# -----------------------------------------------------------
# To value pair in ascending order of keys
'''
a = {"IN":"India", "ES":"Español", "AUS":"Australia", "WI":"West Indies"}
# print(sorted(a, key=a.get))
# Ordering doesn't sort the dict. It returns an ordered list of (key:value) tuples.
print("Sorted print:",sorted(a.items(), key=lambda x: x[1]))
print("Reversed print:",sorted(a.items(), key=lambda x: x[1], reverse=True))
print("Dict as obtained:", a)
'''
# -----------------------------------------------------------
# Single line function and execution : map & lambda & filter
'''
map_out = map(lambda x : x*2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
print("Map Object", map_out)      # Output: map object : <map object at 0x04D6BAB0>
list_map_output = list(map_out)   # Can force convert the map output
print("Product List:", list_map_output)

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
filter_list = list((filter(lambda x : x['name'] == 'python', dict_a)))  
print("Filtered data:", filter_list)    # Output: [{'name': 'python', 'points': 10}]
'''
# -----------------------------------------------------------
# Reverse a list:
'''
a = [1, 33, 7, 99, 453]
print("List:", a)
print("Rev List with index method:", a[::-1])    # [start:stop:step]” pattern
print("Rev List with reversed() method:", list(reversed(a)))

print("reversed List:", a.reverse())  # Returned None, but modified the original list object
print("After reverse call:", a)
'''
# -----------------------------------------------------------
# Merge dictionary:
'''
x = {'a': 1, 'b': 2}
y = {'aa': 11, 'bb': 22}
z = {**x, **y}
print("Merged Dictionary:", z)
'''
# -----------------------------------------------------------
# Difference between del, remove and pop on lists
'''
https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists#answer-11520540
'''
# -----------------------------------------------------------
# Remove all occurrences of an element in the list
'''
x = [1, 2, 3, 4, 2, 2, 3]
print("List BEFORE removing element 2:", x)
while 2 in x: x.remove(2)
print("List AFTER removing element 2:", x)
'''
# -----------------------------------------------------------
# Dictionary: get the key based on the value
'''
search_age = 21
mydict = {'george':16, 'amber':19, 'mike':21}
print("Method 1:", list(mydict.keys())[list(mydict.values()).index(search_age)])  # Prints george

# (OR)
for name, age in mydict.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == search_age:
        print("Method 2:", name)
'''
# -----------------------------------------------------------
# Enumerate:
'''
# Python’s built-in enumerate function allows us to loop over a list,
# and retrieve both the index and the value of each item in the list:
# whenever we need item indexes while looping, we should think of enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):   # Index-Value pair wil be returned
    # print("President {}: {}".format(num, name))
    print("President", num ,":", name)
'''
# -----------------------------------------------------------
# Zip:
'''
# Python’s zip function allows us to loop over multiple lists at the same time.
# Helpful where order is significant proceed with list comprehensions.
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))
'''
# -----------------------------------------------------------
# List Comprehensions:
# An elegant way to define and create lists based on existing lists.
# Syntax: [ expression for item in list if conditional ]
'''
string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)

ad = [x+y for x in [10,30,50] for y in [20,40,60]]
print(ad)
'''
# -----------------------------------------------------------
# Compare two lists
'''
a = [1, 2, 3, 4, 5, 8, 7, 6, 5]
b = [9, 8, 7, 6, 5, 9, 9, 8]
print("List A:", a, "\nList B:", b)
# comm = set(a) & set(b)  -- Possible (May be slower)
comm = set(a).intersection(b)
ext_a = set(a) - set(b)
ext_b = set(b) - set(a)

print("Common elements:", comm)
print("Present in A not in B:", ext_a)
print("Present in B not in A:", ext_b)

# (OR)
# If order is significant you can do it with list comprehensions like this
a = [1, 2, 3, 4, 5, 7, 6]
b = [9, 8, 7, 6, 5, 9, 9]
uni_list = [i for i, j in zip(a, b) if i in b]
print("\nCommon elts without order change:", uni_list)
'''
# -----------------------------------------------------------
