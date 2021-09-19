"""
Generate Fibo series with upper limit and range calls
"""


def fibo(arg1):
    a, b = 0, 1
    while a < arg1:
        yield a
        a, b = b, a + b


fibo_list = []
for i in fibo(30):
    fibo_list.append(i)

print("With upper limit 30", fibo_list)

# ==========================>>


def fibo_2(v_count):
    a, b = 0, 1
    for i in range(v_count):
        yield a
        a, b = b, a + b


fib2 = []
for y in fibo_2(10):
    fib2.append(y)

print("With range 10 : ", fib2)
# ==========================>>

"""
Output:
With upper limit 30 [0, 1, 1, 2, 3, 5, 8, 13, 21]
With range 10 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
