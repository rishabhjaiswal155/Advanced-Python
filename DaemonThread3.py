#Once the last non Daemon Thread execution completes,all Daemon Thread also terminates automatically

from threading import *
import time
def display():
	for t in range(10):
		print(current_thread().name,"is executing...") #Here this Thread is Daemon Thread
		time.sleep(1)
		
t=Thread(target=display,name='Child Thread')
t.setDaemon(True)
t.start()
time.sleep(2)
print(current_thread().name,"'s execution is complete which is last non Daemon Thread..All Daemon Thread execution terminates automatically....")
