#Interface in Python
#Interface is an pure Abstract class which contains only Abstract method.
#Technically Interface is not available in Python,we can create it using class only.
from abc import *
class Interface(ABC): #This is Interface
	@abstractmethod
	def m1(self):
		pass
	@abstractmethod
	def m2(self):
		pass
	@abstractmethod	
	def m3(self):
		pass
	@abstractmethod
	def m4(self):
		pass

#Interface vs Abstract class vs Concrete class:

'''1.Interface:
	It is used when we have only requirement plan and not the implemenation.
i.e It contain only Abstract method.

2.Abstract class:
	It is used when we doesnot have complete Implementation i.e we have partial Implementation
i.e It may contain both Abstract method and Concrete method.

3.Concrete Class:
	It is used when we have Complete Implementation
i.e It contain all concrete Method and not Abstract method.'''
