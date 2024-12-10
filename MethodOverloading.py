#Method Overloading
#Method Overloading is not available in python

class Test14:
	def m1(self):
		print("No argument method")
	
	def m1(self,a):
		print("One argument method")
		
t=Test14()
#t.m1() #These gives error as it executes only the most recent defined method
t.m1(10)