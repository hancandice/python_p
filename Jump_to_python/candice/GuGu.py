# GuGu



y = 5
while True:
    list = []
    number = int(input("Insert the number you want to try: "))
    for i in range(1,10):
        x = number*i
        list.append(x)
    print(list)
    y -= 1
    if y == 0:
        break



def GuGu(number):
    list = []
    for i in range(1,10):
        x = int(number)*i
        list.append(x)
    return list 


