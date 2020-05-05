# coffee.py

coffee = 10
while True :
    money = int(input("Please put your money: "))
    if money == 300:
        print("Here's your coffee.")
        coffee = coffee-1
    elif money > 300:
        print("Here's your coffee, and take your %d change." %(money-300))
        coffee = coffee-1
    else :
        print("I'm sorry but we cannot sell coffee for you. And take your money %d back." % money)
    if coffee ==0:
        print("We ran out of coffee. No sales anymore.")
        break

    
