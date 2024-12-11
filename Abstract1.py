#Example of Abstract class Vehicle
from abc import *
class Vehicle(ABC): #Abstract class
	@abstractmethod
	def get_No_Of_Wheels(self): #Abstract method
		pass

class Bus(Vehicle):
	def get_No_Of_Wheels(self):
		return 7

class Car(Vehicle):
	def get_No_Of_Wheels(self):
		return 5
		
class Auto(Vehicle):
	def get_No_Of_Wheels(self):
		return 3

b=Bus()
print(b.get_No_Of_Wheels())
c=Car()
print(c.get_No_Of_Wheels())
a=Auto()
print(a.get_No_Of_Wheels())