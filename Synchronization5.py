#Acheiving Synchronization using Semaphore:
#In Semaphore, Multiple threads can enter in critical ssection at a time
#s=Semaphore(count) Here Default value of Count is 1 i.e It Behaves as a Lock()
#In Semaphore,number of release calls can exceed the number of acquire calls,thus it is also called as unbounded Semaphore.

from threading import *
import time
s=Semaphore(2)# Here count=2 i.e at a time 2 thread can enter
def wish(name):
    s.acquire() #Whenever we call for acquire then count-1
    for i in range(5):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
    s.release() #Whenever we call for release then count+1
    s.release()
    s.release()
    s.release()
t1=Thread(target=wish,args=('Rishabh',))
t2=Thread(target=wish,args=('Amol',))
t3=Thread(target=wish,args=('Shreyash',))
t1.start()
t2.start()
t3.start()

        
