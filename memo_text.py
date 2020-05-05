
f = open("/Users/candicehan/Documents/practice/newfile1.txt","r")
contents = f.read()
f.close()

x = contents.replace("java","python")

print(x)

f1 = open("/Users/candicehan/Documents/practice/newfile1.txt","w")
f1.write(x)
f1.close()




f2 = open("/Users/candicehan/Documents/practice/newfile1.txt","r")

while True:
    contents = f2.readline()
    print(contents)
    print('\n')
    if not contents : break

    
