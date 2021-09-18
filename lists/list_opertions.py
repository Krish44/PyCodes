# list comprehension
#-----------------------
print("Print square of elements in the list")
l1 = [1,2,3,4,5]
print([x*x for x in l1])
"""
Output:
[1, 4, 9, 16, 25]
"""

##========================================================>>
# lambda
#----------


##========================================================>>
# Join 
# ----------
a_list = ["a", "b", "c"]
joined_string = "\n".join(a_list)
print(joined_string)

"""
Output:
a
b
c
"""
##========================================================>>
# map
#----------
print("For converting elements in list to string")
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join(map(str, s))
print(listToStr)

"""
Output:
'I want 4 apples and 18 bananas'
"""

# map(fun, iter)
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

"""
Output:
[2, 4, 6, 8]
"""

##========================================================>>
# Convert list to string:
l3=["Convert", "this", "to", "string"]
to_string = ' '.join(l3)
print(to_string)
"""
Output:
Convert this to string
"""

