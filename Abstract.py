#Abstract method: A method without implementation or dummy implementation with @abstractmethod decorator from abc module(Abstract Base Class module)
#Abstract Classes:A class having Zero or more Abstract Method and extended from ABC Class of abc module.

from abc import * #importing abc module
class Vehicle(ABC): #Abstract Class
	@abstractmethod
	def get_No_Of_wheels(self): #Abstract method
		pass

class Fruit(ABC): #Abstract class
	@abstractmethod
	def get_taste(self): #Abstract Method
		pass

#If a class is Abstract and have atleast one abstract method then instantiation is not possible

#v=Vehicle() #These gives error
#f=Fruit() #These gives error
