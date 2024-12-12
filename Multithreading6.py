#MultiThreading example with doubles and squares functionality executed by two seperate threads.
from threading import *
import time
def doubles(numbers):
	for i in numbers:
		print("Double:",i*2)
		time.sleep(1)

def squares(numbers):
	for i in numbers:
		print("Square:",i*i)
		time.sleep(1)
		
numbers=[1,2,3,4,5,6]
beginTime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join() #Here main thread is waiting for t1 and t2 to completes its execution 
t2.join()
endTime=time.time()
print("The Total time taken:",endTime-beginTime)
		
