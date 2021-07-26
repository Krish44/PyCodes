"""
Create a calculator program using classes
"""


class maths():
    def __init__(self ,arg1 ,arg2):
        self.param1 = arg1
        self.param2 = arg2

    def add(self):
        print(self.param1 + self.param2)

    def mul(self):
        print(self.param1 * self.param2)


# Create instance of class
obj = maths(2,3)
# Create method
obj.add()
obj.mul()

"""
Output:
5
6
"""
