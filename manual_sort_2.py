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
