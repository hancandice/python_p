# Kom visited Cafe J

espresso = 10

print ("Hello, Kom! Welcome to Cafe J! You should try our espresso!")
print ("You want to try our new version of espresso?")

while True :
    print ("How much can you pay for our espresso?")
    money = int(input("please input your money here. "))
    if money > 3:
        print("Take your coffee! Thank you, enjoy it!")
        espresso = espresso-1
        print("And here's your change. %d" % (money-3))
    elif money == 3:
        print("Take your coffee! Thank you, Kom. Enjoy it!")
        espresso = espresso-1
    else :
        print("No, our espresso is more expensive than the money you gave us. Take your money back.")
        print("Here is your money. %d" % money)
    if espresso ==0:
        print("Oh, I'm sorry. Our espresso was just sold out. See you next time!")
        break

                
