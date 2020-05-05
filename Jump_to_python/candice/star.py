x=1
y=int(input("How many stars do you want to put? "))
z=3
while True :
    if x<=y:
        print("*"*x)
        x=x+1
    else:
        z=z-1
        if z==0: break
        y=int(input("Again! How many stars do you want to put? "))
        x=1

