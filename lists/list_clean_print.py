"""
Print list content without square braces
"""

l1 = ["Red", "Yellow", "Blue", "Green"]
print("Original:", l1)
print("Without map function, since strings:", ', '.join(l1))

l2 = [3, 4, 5, 76, 8, 1, 78, 3, 5, 7]
print("Original:", l2)
print("With map function, since integers:", ', '.join(map(str,l2)))

"""
Output:
Original: ['Red', 'Yellow', 'Blue', 'Green']
Without map function, since strings: Red, Yellow, Blue, Green
Original: [3, 4, 5, 76, 8, 1, 78, 3, 5, 7]
With map function, since integers: 3, 4, 5, 76, 8, 1, 78, 3, 5, 7
"""
