print("{0:=^80}".format('Lv.1'))

#. Multiples of 3 and 5

x = 0

for n in range(1,1001):
    
    if n%3==0 or n%5==0:
        x+=n

print(x)


print(sum([n for n in range(1001) if n%3==0 or n%5==0]))

set_3 = set(range(3,1001,3))
set_5 = set(range(5,1001,5))

print(sum(set_3|set_5))


#. Tab to 4space

data = '''
for n in range(1,1001):
    if n%3==0 or n%5==0:
        x+=n'''

def tabto4space(data):
    list = data.split("\t")
    list2=[]
    for word in list:
        list2.append(word)
        list2.append("\t")
    x = "".join(list2).strip()
    return x


#. Total page numbers

def totalpage(m,n):
    if m%n==0:
        return m/n
    else:
        return m//n+1


def totalpage2(m,n):
    result = m//n+1
    if m%n==0:
        result -= 1
    return result

#. 사이냅 소프트 기출

question = '''주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

"이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

- 김씨와 이씨는 각각 몇 명 인가요?
- "이재영"이란 이름이 몇 번 반복되나요?
- 중복을 제거한 이름을 출력하세요.
- 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.'''


names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
names_list = names.split(',')

import re
pk = re.compile(r"김\w+")
pl = re.compile(r"이\w+")

list_kim = []
list_lee = []

for name in names_list :
    m = pk.match(name)
    try:
        list_kim.append(m.group())
    except AttributeError:
        pass

for name in names_list :
    n = pl.match(name)
    try:
        list_lee.append(n.group())
    except AttributeError:
        pass

#. - 김씨와 이씨는 각각 몇 명 인가요?
len(set(list_kim))
len(set(list_lee))

#. - "이재영"이란 이름이 몇 번 반복되나요?
names_list.count('이재영')

#. - 중복을 제거한 이름을 출력하세요.
set(names_list)

#. - 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
list(set(names_list)).sort()


#. Special sort(Google telephone interview)

# input -1 1 3 -2 2 ans -1 -2 1 3 2



def specialsort(numbers):
    list2 = []
    list3 = []
    list = numbers.split(" ")
    
    for number in list:
        if int(number)<0:
            list2.append(number)
        else:
            list3.append(number)
    list2.extend(list3)
    return " ".join(list2)


# next ? The Knights Of The Round Table






            
    
    









    
    


