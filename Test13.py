#Destructor
import time
class Test13:
	def __init__(self):
		print("Object initialize....")
		
	def __del__(self): #Destructor
		print("Performing cleanup activities....")
		
t1=Test13()
t2=t1
t3=t2
del t1 #deleting reference variable
time.sleep(5)
del t2 #deleting reference variable
time.sleep(5)
del t3 #deleting reference variable and object marked for GC
time.sleep(5)
print("End of Application....")