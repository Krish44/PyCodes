#
# Reverse a given string and see if it is a palindrome
# Print the result if its a palindrome
#

def check_palindrome(in_list):
    for v_index, v_value in enumerate(in_list):
        v_value = v_value.lower()
        # if v_value == v_value[::-1]:
        # [OR] use below condition
        if v_value == "".join(reversed(v_value)):
            print("Index:",v_index, "Value:", v_value)


my_list = ['string1','pop','Malayalam','nitin','spoon']
check_palindrome(my_list)

"""
OutPut:
-------
Index: 1 Value: pop
Index: 2 Value: malayalam
Index: 3 Value: nitin
"""
