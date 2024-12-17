#Good Programming Practices:
#1.Always release the lock in finally block

from threading import *
import time
l=Lock()
def wish(name):
	l.acquire()
	try:
		for i in range(5):
			print("Good Evening:",flush=True,end='')
			time.sleep(2)
			print(name)
	finally:
		l.release()
t1=Thread(target=wish,args=('Rishabh',))
t2=Thread(target=wish,args=('Amol',))
t3=Thread(target=wish,args=('Shreyash',))
t1.start()
t2.start()
t3.start()


