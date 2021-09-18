"""
Check if elementrs repeated odd or even number of times

"""

v_list = [2,2,2,5,5,4,4,4,3,3,1,1,1]
# Convert to set since set keeps uniq elements
v_set = set(v_list)
print("Converted to set:", v_set)

# Check for repetitions for set element in list
for item in v_set:
    print(item,"repeated",v_list.count(item),"times")
    if v_list.count(item) % 2 != 0:
        print("   -- has odd repeats")

"""
Output:
Converted to set: {1, 2, 3, 4, 5}
1 repeated 3 times
   -- has odd repeats
2 repeated 3 times
   -- has odd repeats
3 repeated 2 times
4 repeated 3 times
   -- has odd repeats
5 repeated 2 times
"""
