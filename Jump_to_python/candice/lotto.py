# lotto numbers

import time
import random

z = 3
x = input("Hello, what's your name? ")
time.sleep(0.5)
print("Hi %s, your lucky numbers are ready for you!" %x)
time.sleep(2)
while True:
    y = input("Shall we start? (Answer in yes or no) ")
    if y == 'yes':
        lotto = []
        time.sleep(1)
        while len(lotto)<6:
            number = random.randint(1,45)
            if number not in lotto:
                lotto.append(number)
        print("Your lucky numbers are ... ")
        time.sleep(1.5)        
        print(lotto)
        z = z-1
        time.sleep(1.5)
        if z != 0:
            print("You want to try it again? :) You still can try %d time(s) more." %z)
            time.sleep(2)   
    elif y == 'no' :
        print("Ok. Then good bye! Have an awesome day!")
        break
    elif y != 'yes' and y != 'no':
        print("Plesae answer properly. ")
        time.sleep(1.5)
        pass
    if z == 0:
        time.sleep(0.5)
        print("And...")
        time.sleep(1)
        print("Oh :( It's time to say good bye...")
        time.sleep(1)
        print("It was very good time with you, %s! Hope to see you next time." %x)
        time.sleep(1)
        print("Have a beautiful day!")
        break

        
