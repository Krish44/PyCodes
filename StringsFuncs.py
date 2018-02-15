import string
import random

print(dir(string))  # will list all available methods
print("Prints ASCII letters: ", string.ascii_letters)
StringSet = string.ascii_lowercase
print("ASCII lower: ", StringSet)

print(random.choice(StringSet))
