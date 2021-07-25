list_1 = [2, 9, 66, 5, 3, 1]
print(list_1)
v_len = len(list_1)

for i in range(v_len):
    for v_index, v_value in enumerate(list_1):
        try:
            if v_value > list_1[v_index+1]:
                list_1.pop(v_index)
                list_1.insert(v_index + 1, v_value)
                print("Intermediary moves:", list_1)
        except IndexError:
            break

print("Final Sorted:", list_1)
print("reverse via slicing:", list_1[::-1])
print("reversed via function:", [data for data in reversed(list_1)])
list_1.reverse()
print("Reversed Inline:", list_1)


"""
Output: 
[2, 9, 66, 5, 3, 1]
Intermediary moves: [2, 9, 5, 66, 3, 1]
Intermediary moves: [2, 9, 5, 3, 66, 1]
Intermediary moves: [2, 9, 5, 3, 1, 66]
Intermediary moves: [2, 5, 9, 3, 1, 66]
Intermediary moves: [2, 5, 3, 9, 1, 66]
Intermediary moves: [2, 5, 3, 1, 9, 66]
Intermediary moves: [2, 3, 5, 1, 9, 66]
Intermediary moves: [2, 3, 1, 5, 9, 66]
Intermediary moves: [2, 1, 3, 5, 9, 66]
Intermediary moves: [1, 2, 3, 5, 9, 66]
Final Sorted: [1, 2, 3, 5, 9, 66]
reverse via slicing: [66, 9, 5, 3, 2, 1]
reversed via function: [66, 9, 5, 3, 2, 1]
Reversed Inline: [66, 9, 5, 3, 2, 1]

"""
