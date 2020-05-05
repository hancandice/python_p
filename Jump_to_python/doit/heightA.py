
A=[170, 160, 155, 175, 195, 190, 180, 180, 185, 200]
b=0
for a in A:
    b=b+a
    
average=b/len(A)

print(average)
    

y=0

while True:
    if (b+y)/(len(A)+1)< 180:
        y=y+0.001
    else:
        print(y)
        break

        
    
