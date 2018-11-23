"""
To execute some shell commands for python program
https://www.journaldev.com/16140/python-system-command-os-subprocess-call
"""

import os
import subprocess

cmd = "git --version"

# Execute unix system command using system module:
returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)

cmd2 = "ls| cut -d \'.\' -f2 | sort -u "
direct = os.system(cmd2)
print("Content:", direct)
# Only execution status can be captured in the return, variable does not hold the result of shell command

# Trying similar execution using subprocess.call()
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)

# Try storing the value to a variable using subprocess.check_output()
cmd4 = "date"

# returns output as byte string
returned_output = subprocess.check_output(cmd4)

# using decode() function to convert byte string to string
print('Current date is:', returned_output.decode("utf-8"))
