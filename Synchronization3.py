#solving the Problem having with Synchronization using Lock() by using RLock():
from threading import *
l=RLock()
print("Main Thread trying to acquire lock..")
l.acquire()
print("Main Thread trying to acquire lock again..")
l.acquire()
print("Main Thread acquire the same lock again..")
l.release()
l.release()
