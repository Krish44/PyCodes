"""
Python generators:
1. Generate even number range
2. generate fibonacci series

"""
print("<<================================>>")
print("Generate even numbers:")

def get_even(n):
    n = n*2
    yield n

print("Print upto range: 10")
for i in range(0,10):
    num = get_even(i)
    print(next(num), end=" ")
print("\n<<================================>>")


print("Generate Fibo series:")

def fibo(limit):
        a,b = 0,1
        while a < limit:
            yield a
            a,b = b, a+b

print("Display fibo numbers till 50")

for i in fibo(50):
    print(i, end=" ")

print("\n<<================================>>")

"""
Output:
<<================================>>
Generate even numbers:
Print upto range: 10
0 2 4 6 8 10 12 14 16 18 
<<================================>>
Generate Fibo series:
Display fibo numbers till 50
0 1 1 2 3 5 8 13 21 34 
<<================================>>
"""


