#Daemon Threads and its methods like isDaemon(),setDaemon()
from threading import *
print(current_thread().name,"is Daemon:",current_thread().isDaemon()) #only main Thread is non Daemon
#OR
print(current_thread().name,"is Daemon:",current_thread().daemon) #daemon is implicit variable to check whether Thread is Daemon or not.
#current_thread().setDaemon(True) #method to change the nature of Thread
#Once the Thread is started its nature cannot be changed.
#Also Main Thread is non Daemon and not possible to change its nature.