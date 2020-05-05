# /Users/candicehan/Documents/doit/memo.py


import sys

option = sys.argv[1]


if option == '-a':
    memo = sys.argv[2]
    f = open("/Users/candicehan/Documents/doit/memo.txt",'a')
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':
    y = open("/Users/candicehan/Documents/doit/memo.txt")
    memo = y.read()
    y.close()
    print(memo)


    
    
