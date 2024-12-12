#Creating a thread by creating a class without extending from Thread class.
from threading import *
class MyThread:
	def display(self):
		for i in range(10):
			print("Child Thread executed by:",current_thread().name,"for",i,"time")
obj=MyThread()
t=Thread(target=obj.display)
t.start()
for i in range(10):
	print("Main Thread executed by:",current_thread().name,"for",i,"time")
	
