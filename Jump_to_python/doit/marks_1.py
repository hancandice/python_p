# marks1.py
marks = [90, 25, 67, 35, 80]

number = 0
for mark in marks :
    number = number+1
    if mark>60:
        print("student number%d has passed the exam" % number)
        print("Congratulation!")
    else:
        print("Student number%d hasn't passed the exam" %number)
        print("I'm sorry but student number %d has to take this exam again." %number)


    
