#Three ways to Create a Thread
#1.without using any class

from threading import *
def display():
	for i in range(10):
		print("Child Thread executed by:",current_thread().name,"for",i,"time")
t=Thread(target=display)
t.start()
for i in range(10):
	print("Main Thread executed by:",current_thread().name,"for",i,"time")
