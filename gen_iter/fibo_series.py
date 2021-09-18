"""
Print fibonacci series for nth element:
Python Program for n-th Fibonacci number
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2 With seed values F0 = 0 and F1 = 1.
"""

Fn = int(input("Enter nth element of the fibo series: "))

fibo_series = [0, 1]
for i in range(2, Fn):
    new_element = fibo_series[i-1] + fibo_series[i-2]
    fibo_series.append(new_element)

print("Generated fibo series:", fibo_series)
print(Fn, "nth element of the fibo series is:", fibo_series[Fn-1])


"""
Output:
--------
Enter nth element of the fibo series: 14
Generated fibo series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
14 nth element of the fibo series is: 233

"""
