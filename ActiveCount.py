#active_count() in threading module to count the number of threads active.

from threading import *
import time
def display():
	print(current_thread().name,"stared...")
	time.sleep(3)
	print(current_thread().name,"ended...")
t1=Thread(target=display,name='Child Thread1')
t2=Thread(target=display,name='Child Thread2')
t3=Thread(target=display,name='Child Thread3')
print("Number of Active Threads:",active_count())
t1.start()
t2.start()
t3.start()
print("Number of Active Threads:",active_count())
time.sleep(4)
print("Number of Active Threads:",active_count())


	