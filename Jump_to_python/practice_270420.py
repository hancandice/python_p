

list = []
x = 0
for i in range(1,1000):
    if i%3==0 or i%5 ==0:
        list.append(i)
        x = x+i

print(list)

print(x)


