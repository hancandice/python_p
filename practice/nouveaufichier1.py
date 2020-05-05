

f = open("/Users/candicehan/Documents/practice/newfile1.txt","w")

for i in range(1,16):
    x = "This is line number %d.\n" %i
    f.write(x)

f.close()



for t in range(1,11):
    y = "This is line number %d.\n" %t
    print(y)

    
