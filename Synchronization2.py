#Problem with Synchronization using Lock():
from threading import *
l=Lock()
print("Main Thread trying to acquire lock..")
l.acquire()
print("Main Thread trying to acquire lock again..")
l.acquire() #Here Program halts as main thread is acquiring same lock again
print("Main Thread acquire the same lock again..")

#Lock() cannot be used in case of Nested Access or Recursive Function if multiple times lockmis getting acquired.