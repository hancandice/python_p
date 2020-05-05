print("{0:=^70}".format(' Question 10 '))

import os

os.chdir("/Users/candicehan/Documents/doit")
f = os.popen("ls")
print(f.read())

print("{0:=^70}".format(' Question 11 '))

import glob
print(glob.glob("/Users/candicehan/Documents/doit/*.py"))

print("{0:=^70}".format(' Question 12 '))

import time
time.ctime()


print("{0:=^70}".format(' Last Question '))

import random
lotto = []

while len(lotto)<6:
    x = random.randint(1,45)
    
    if x not in lotto:
        lotto.append(x)

        
