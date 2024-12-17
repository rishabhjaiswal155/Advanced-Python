#Interthread Communication using Condition Object:
#This ITC using Condition Object internally uses RLock().
from threading import *
def produce(c):
		c.acquire()
		print("Producer Thread producing the item...")
		print("Producer Thread Sending the notification..")
		c.notify()
		c.release()
def consume(c):
		c.acquire()
		print("Consumer Thread waiting for Notification....")
		c.wait()
		print("Consumer Thread got Notification...")
		print("Consumer Thread Consuming the item...")
		c.release()
c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()

		