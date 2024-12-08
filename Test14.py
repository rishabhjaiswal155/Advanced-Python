import time
class Test14:
	def __init__(self):
		print("Object initialize....")
		
	def __del__(self): #Destructor
		print("Performing cleanup activities....")
		
list=[Test14(),Test14(),Test14()] #list reference variable pointing to the list of objects
del list #deleting list reference variable and marked the list object for GC
time.sleep(5)
print("End of Application.....")