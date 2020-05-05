

print("{0:=^70}".format(' Bien Joue '))



f1 = open("/Users/candicehan/Documents/practice/newfile1.txt","r")
lines = f1.readlines()


for line in lines:
    print(line)

f1.close()





# 3.

f = open("/Users/candicehan/Documents/practice/newfile1.txt","r")
data = f.read()
print(data)
f.close()




# adddata.py


f = open("/Users/candicehan/Documents/practice/newfile1.txt","a")

for i in range(16,31):
    data = "This is line number %d.\n" %i
    f.write(data)

f.close()    


