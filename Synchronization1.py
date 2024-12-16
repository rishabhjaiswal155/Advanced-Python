#Synchronization using Lock() to solve the Problem of data inconsistency
from threading import *
import time
l=Lock() #Synchronization using Lock()
def wish(name):
    l.acquire() #acquiring the lock
    for i in range(10):
        print("Good Evening:",end='') #line number 6-9 is critical section
        time.sleep(2)
        print(name)
    l.release() #releasing the lock
t1=Thread(target=wish,args=('Rishabh',))
t2=Thread(target=wish,args=('Vishal',))
t3=Thread(target=wish,args=('pranav',))
t4=Thread(target=wish,args=('Mauli',))
t1.start()
t2.start()
t3.start()
t4.start()
