#Good Programming Practices:
#2.use with keyword thus no need to explicitly acquire and release the lock.

from threading import *
import time
l=Lock()
def wish(name):
	with l:
		for i in range(5):
			print("Good Evening:",flush=True,end='')
			time.sleep(2)
			print(name)

t1=Thread(target=wish,args=('Rishabh',))
t2=Thread(target=wish,args=('Amol',))
t3=Thread(target=wish,args=('Shreyash',))
t1.start()
t2.start()
t3.start()


