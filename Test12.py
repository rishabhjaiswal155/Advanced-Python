#Destructor
import time
class Test12:
	def __init__(self):
		print("Object initialize....")
		
	def __del__(self): #Destructor0000
		print("Performing cleanup activities....")
		
t=Test12()
t=None
time.sleep(5)
print("End of Application....")