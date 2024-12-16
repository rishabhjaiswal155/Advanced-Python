#enumerate() in threading module to enumerate the list of thread one by one and print thread information

from threading import *
import time
def display():
	print(current_thread().name,"stared...")
	time.sleep(3)
	print(current_thread().name,"ended...")
t1=Thread(target=display,name='Child Thread1')
t2=Thread(target=display,name='Child Thread2')
t3=Thread(target=display,name='Child Thread3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
	print(t.name)
	print(t.ident)
time.sleep(4)
l=enumerate()
for t in l:
	print(t.name)
	print(t.ident)
