# thread_with_run

# thread_without_run_method


from threading import Thread
import time

def My_thread(x):
    for _ in range(3):
        print("I'm Thread")
        time.sleep(2)

a = Thread(target=My_thread,args=(1,))
a.start()
a.join()

for i in range(3):
    print("I'm real Thread")
    time.sleep(1)
    
print("---The End---")


