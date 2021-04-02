# Dict select: Print out number 10 only from the following dictionary.
money = {"saving_account":200, "checking_account": 100, "under_bed": [500,10,100]}
print(money["under_bed"][0])

# Key search: Iterate through a list, print only on keyword match
MailList = ['one@gmail.com','two@ymail.com','ten@gmail.com']
for item in MailList:
    key = 'ymail'
    if key in item:
        print(item)

# Password test: Using While loop
passwd = ''
while passwd != 'Code345':
    key = input("Enter the password: ")
    if key == 'Code345':
        print("You are logged in")
    else:
        print("Oops..!! Error  in password. Try again")
    passwd = key

# Multiple list - zip:
mails = ['one@gmail.com','two@ymail.com','ten@gmail.com']
names = ['One', 'Two', 'Ten']

for i,j in zip(names,mails):
    print(i,j)

# Looping in a list
a="Tricky"
for i in a[:3]:
    print(i)

# Takes a single element list and breaks it
lst=["Terribly Tricky"]
print("Before: ",lst[-1])
for word in lst:
    print(word)
    for letter in word[-6:]:
        print(letter)

"""
Output:
500
two@ymail.com
Enter the password: Code345
You are logged in
One one@gmail.com
Two two@ymail.com
Ten ten@gmail.com
T
r
i
Before:  Terribly Tricky
Terribly Tricky
T
r
i
c
k
y
"""
