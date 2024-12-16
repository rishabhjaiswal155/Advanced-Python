#is_alive() in Thread class returns True if Thread is alive else returns False.
from threading import *
import time
def display():
	print(current_thread().name,"stared...")
	time.sleep(3)
	print(current_thread().name,"ended...")
t1=Thread(target=display,name='Child Thread1')
t2=Thread(target=display,name='Child Thread2')
t3=Thread(target=display,name='Child Thread3')
t1.start()
t2.start()
t3.start()
print(t1.name,"is alive:",t1.is_alive())
print(t2.name,"is alive:",t2.is_alive())
print(t3.name,"is alive:",t3.is_alive())
time.sleep(4)
print(t1.name,"is alive:",t1.is_alive())
print(t2.name,"is alive:",t2.is_alive())
print(t3.name,"is alive:",t3.is_alive())
