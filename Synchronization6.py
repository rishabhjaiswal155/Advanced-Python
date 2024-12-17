#Acheiving Synchronization using BoundedSemaphore:
#In BoundedSemaphore, Multiple threads can enter in critical section at a time
#s=BoundedSemaphore(count) Here Default value of Count is 1 i.e It Behaves as a Lock()
#In BoundedSemaphore,number of release calls cannot exceed the number of acquire calls,thus it is also called as bounded Semaphore.

from threading import *
import time
s=BoundedSemaphore(2)# Here count=2 i.e at a time 2 thread can enter
def wish(name):
    s.acquire() #Whenever we call for acquire then count-1
    for i in range(5):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
    s.release() #Whenever we call for release then count+1
t1=Thread(target=wish,args=('Rishabh',))
t2=Thread(target=wish,args=('Amol',))
t3=Thread(target=wish,args=('Shreyash',))
t1.start()
t2.start()
t3.start()

        
