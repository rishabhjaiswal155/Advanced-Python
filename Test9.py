#Program to count the number of objects created for a particular class
class Test9:
	count=0 #static variable
	def __init__(self):
		Test9.count=Test9.count+1
	
	@classmethod #class method
	def countNoOfObjectsCreated(cls):
		print("Number of Objects Created:",cls.count) #Accessing static varaible using cls variable
		
t=Test9()
t1=Test9()
Test9.countNoOfObjectsCreated() #calling class method using classname
t2=Test9()
t3=Test9()
Test9.countNoOfObjectsCreated() #calling class method using classname
