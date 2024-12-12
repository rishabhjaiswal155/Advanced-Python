#MultiThreading,threading module current_thread().getName() and current_thread().setName()
#getName() and setName('') are deprecated instead use name attribute
from threading import *
print("This Code is Executed by:",current_thread().getName())
current_thread().setName('Rishabh')
print("This Code is Executed by:",current_thread().getName())

