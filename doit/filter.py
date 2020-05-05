# positive.py

def positive(I):
    result = []
    for i in I:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))


# filter1.py

def positive(x):
    return x > 0


print(list(filter(positive,[1,-3,2,0,-5,6])))

print(list(filter(positive,[1,-3,2,0,-5,6])))


list(filter(lambda x : x>0, [1,-3,2,0,-5,6]))
