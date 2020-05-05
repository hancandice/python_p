# thread_test.py

import threading
import time

x = ['sleeps','smiles','studies','makes love','takes a shower']

def Jeeyoung():
    for i in x:
        time.sleep(1)
        print("Jeeyoung is pretty when she %s.\n" %i)
        
print("Start")

z=[]

for _ in range(5):
    y = threading.Thread(target = Jeeyoung)
    z.append(y)

        
for student in z:
    student.start()

for student in z:
    student.join()

print("End")
