from threading import *
class MyThread:
	def display(self):
		for i in range(10):
			print("Child Thread executed by:",current_thread().name,"for",i,"time")
obj=MyThread()
t1=Thread(target=obj.display)
t2=Thread(target=obj.display)
t3=Thread(target=obj.display)
t4=Thread(target=obj.display)
t1.start()
t2.start()
t3.start()
t4.start()
for i in range(10):
	print("Main Thread executed by:",current_thread().name,"for",i,"time")
	
