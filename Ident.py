#Thread Identification Number using implicit variable ident
from threading import *
def display():
	print("Child Thread Identification Number:",current_thread().ident)
t=Thread(target=display)
t.start()
print("Child Thread Identification Number:",t.ident)
print("Main Thread Identification Number:",current_thread().ident)