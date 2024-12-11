#Abstract classes Example
from abc import *
class Test(ABC): #Abstract class
	def m1(self): #Instance method
		print("Hello I am normal method...")

class Test1(ABC): #Abstract class
	@abstractmethod 
	def m1(self): #Abstract method
		pass
	
	def m2(self): #Instance method
		print("Hello I am normal method...")
		
t=Test() #Here Test is Abstract class but doesnot have any abstract method ,Thus instantiation possible.
t.m1() #Valid
#t1=Test1() # Gives Error Here Test1 is Abstract class but also have Abstract method,So Instantiation not possible
#t1.m1() #Gives error
#t1.m2() #Gives error

