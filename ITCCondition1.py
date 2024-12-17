from threading import *
import random
import time
items=[]
def produce(c):
	while True:
		c.acquire()
		item=random.randint(1,100)
		print("Producer producing the item:",item)
		items.append(item)
		print("Producer sending the Notification...")
		c.notify()
		c.release()
		time.sleep(5)
def consume(c):
	while True:
		c.acquire()
		print("Consumer Waiting for the Notification...")
		c.wait()
		print("Consumer Got the Notification...")
		print("Consumer consume the item",items.pop())
		c.release()
		time.sleep(5)
c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()

