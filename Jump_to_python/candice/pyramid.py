"""
Create a half pyramid using hashes
Make sure it's right aligned
It should correspond to the height given by the User
The first line should start with 2"#"s
"""

import time

print("Hello!")

time.sleep(1)

h = int(input("Please choose a number that is 1~30: "))

while (h<1 or h>30):
    print("That is invalid number.")
    h = int(input("please input a valid number. "))

if h==1:
    print("##")

for i in range(2,h+1):
    print(" "*(h-i) + "#"*i + "#"*i + " "*(h-i))
