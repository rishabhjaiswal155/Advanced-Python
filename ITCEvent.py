#Interthread Communication using Event:
#Producer Consumer Example:
from threading import *
import time
e=Event()
def consumer():
	print("Consumer Thread waiting for Updation...")
	e.wait()
	print("Consumer Thread got notification and Consuming items....")
def producer():
	time.sleep(5)
	print("Producer Thread producing items...")
	print("Producer Thread giving notification by setting Event...")
	e.set()
	
t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()
