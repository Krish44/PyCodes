"""
Use of f-strings in multi line statement print
Ref: https://realpython.com/python-f-strings/
"""

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)

print(message)

"""
Output:
Hi Eric. You are a comedian. You were in Monty Python.
"""
