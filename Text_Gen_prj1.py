import string
import random

def text_gen():
    ltr1 = random.choice(string.ascii_lowercase)
    ltr2 = random.choice(string.ascii_lowercase)
    ltr3 = random.choice(string.ascii_lowercase)
    # print(ltr1,ltr2,ltr3)
    print(ltr1+ltr2+ltr3)

for i in range(1,10):
    text_gen()
