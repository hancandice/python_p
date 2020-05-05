

with open("test.txt","w") as f1:
    f1.write("Life is so cool")


f2 = open("test.txt","r")
print(f2.read())


