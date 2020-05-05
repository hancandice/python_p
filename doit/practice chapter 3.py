#. practice chapter 3

a="Life is too short, you need python."

if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")



a=0
b=0
while a<1001:
    if a%3 != 0:
        a = a+1
    else:
        b = b+a
        a = a+1

print(b)


result = 0
i = 1
while i <= 1000:
    if i % 3 ==0:
        result +=i
    i+=1

print(result)



x=0
y=0
while x<=1000:
    if x%3==0:
        y=x+y
    x+=1
    
print(y)


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
        

    
print("""

I love you

""")



i=0
while True :
    i+=1
    if i>5: break
    print("*"*i)

    
print(" ")
    

for x in range(1,11):
    print(x)
    


print(" ")


score = [70,60,55,75,95,90,80,80,85,100]

y=0
for x in score :
    y=y+x

print(y/len(score))


#

A = [70,60,55,75,95,90,80,80,85,100]
total = 0

for score in A:
    total+=score

average = total / len(A)

print(average)




numbers = [1,2,3,4,5]
result = [x*2 for x in numbers if x%2==1]
print(result)



numbers = [1,2,3,4,5]

result = [ ]
for n in numbers:
    if n%2==1:
        result.append(n*2)

print(result)









