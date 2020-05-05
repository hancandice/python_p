data = '''

Jeeyoung Han 921127-2482948
Sehyun Kim 940728-1234958
Minji Jang 950223-2394051
Sora Im 930412-2345293

'''

list2 = []

for line in data.split('\n'):
    list1 = []
    
    for word in line.split(' '):

        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word = word.replace(word[8:],"*"*6)
        list1.append(word)
    list2.append(' '.join(list1))
print('\n'.join(list2))


data2 = '''

Jeeyoung Han 921127-2482948
Sehyun Kim 940728-1234958
Minji Jang 950223-2394051
Sora Im 930412-2345293

'''

import re

test = re.compile("(\d{6})[-]\d{7}")
print(test.sub("\g<1>-*******",data2))
