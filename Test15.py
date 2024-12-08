#to count the number of reference pointing to object
import sys
class Test15:
	def __init__(self):
		print("Object initialize....")
		
	def __del__(self):
		print("Performing cleanup activities....")

t1=Test15()
t2=t1
t3=t2
t4=t3
print("Reference count:",sys.getrefcount(t1))
print("End Of Application and destroying objects by GC")
