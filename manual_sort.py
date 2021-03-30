"""
Sort a given list in ascending/descending order without using sort

"""
l1 = [2,99,88,6,3,9,8,4,6]
l2 = l1.copy()
l2.sort()
print("Sorted using sort:",l2)
print("Sorted desc using sorted:", sorted(l2,reverse=1))
print("Length of list:", len(l1))

for i in range(len(l1)-1):
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            v_big = l1[i]
            l1.pop(i)
            l1.insert(i+1, v_big)

print(l1)
l1.reverse()
print(l1)

"""
Output:
Sorted using sort: [2, 3, 4, 6, 6, 8, 9, 88, 99]
Sorted desc using sorted: [99, 88, 9, 8, 6, 6, 4, 3, 2]
Length of list: 9
[2, 3, 4, 6, 6, 8, 9, 88, 99]
[99, 88, 9, 8, 6, 6, 4, 3, 2]
"""
