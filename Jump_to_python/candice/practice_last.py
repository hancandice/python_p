
x = "4546793"


def DashInsert(data):
    result = []
    x = list(map(int,data))
    for n in range(len(x)):
        result.append(x[n])
        if (len(x)-1) > n:
            if (x[n])%2==0 and (x[n+1])%2==0:
                result.append("*")
            if (x[n])%2!=0 and (x[n+1])%2!=0:
                result.append("-")        
    return "".join(map(str,result))


print(DashInsert(x))        

               
data = "4546793"

numbers = list(map(int,data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:
        is_odd = num%2==1
        is_next_odd = numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")

print("".join(result))
    

print("{0:=^80}".format(":-)"))


def compress_string(input):
    _s = ""
    result = ""
    count = 0
    for s in input:
        if s!=_s:
            if count: result = result + str(count)
            count = 1
            _s = s
            result = result+s
            
        else:
            count = count + 1
    if count: result = result + str(count)
    return result


print(compress_string('aaabbcccccca'))


print("{0:=^80}".format(':-)'))




def check(numbers):
    x = list(map(int,str(numbers)))
    if len(x)==10:
        for n in range(10):
            try:
                x.remove(n)
            except ValueError:
                pass
        if x==[]:
            return True
        else:
            return False
    else:
        return False


print("{0:=^80}".format(':-)'))


def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10


print("{0:=^80}".format('" Q 16 "'))


dic_morse = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
    }

def morse(text):
    result = []
    for word in text.split("  "):
        for letter in word.split(" "):
            result.append(dic_morse[letter])
        result.append(" ")
    return "".join(result).strip()


print("{0:=^80}".format('" Q 17 "'))


import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start()+m.end()


print("{0:=^80}".format('" Q19 Grouping "'))
        

import re

data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

p = re.compile(r"\d+$",re.M)
print(p.sub("****",data))


   
print("{0:=^80}".format('" Q20 Lookahead Assertions "'))











    
        
