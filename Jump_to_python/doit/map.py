# two_times.py

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

x = two_times([1,2,3,4])
print(x)


def two_times(x):
    return x*2

print(list(map(two_times,[1,2,3,4])))


print(list(map(lambda x: x*2,[1,2,3,4])))
