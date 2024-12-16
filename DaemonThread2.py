#Nature of Thread is Inherited from the nature of Its parent Thread.

from threading import *
import time
def job1():
	print("Job1 executes...")
	t2=Thread(target=job2,name='JOB2 Thread') #Here t2 is Daemon Thread as its parent is Daemon 
	print(t2.name,"is Daemon:",t2.daemon)
	t2.start()
def job2():
	print("Job2 executes...")
	time.sleep(2)
t1=Thread(target=job1,name='JOB1 Thread') #Here t1 is non Daemon as its parent is main Thread
t1.setDaemon(True) #Here we change the nature of t1 to Daemon
print(t1.name,"is Daemon:",t1.daemon)
t1.start()
time.sleep(2)
print("End of Application..")
