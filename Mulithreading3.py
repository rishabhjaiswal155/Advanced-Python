#2. creating a thread using class extending from Thread class
from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print("Child Thread executed by:",current_thread().getName(),"for",i,"time")

t=MyThread()
t.start()
for i in range(10):
	print("Main Thread executed by:",current_thread().getName(),"for",i,"time")

	
