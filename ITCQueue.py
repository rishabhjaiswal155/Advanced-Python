#Interthread Communication using Queue Object
#Queue internally uses Condition and Condition internally uses Lock(),thus we don't require to acquire and release the lock,also doesn't need to wait and notify
#only put() and get() performs all like wait,acquire,release,notify...
from threading import *
import time
import random
import queue #importing queue for using Queue Object.
def produce(q):
	while True:
		print("Producer waiting for Updation...")
		item=random.randint(1,11)
		print("Producer Producing the item:",item)
		print("Producer putting in onto Queue...")
		q.put(item)
		time.sleep(5)

def consume(q):
	while True:
		print("Consumer waiting for notification....")
		print("Consumer consuming the item:",q.get())
		time.sleep(5)

q=queue.Queue()
t1=Thread(target=consume,args=(q,))
t2=Thread(target=produce,args=(q,))
t1.start()
t2.start()

