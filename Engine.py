#Member of one class used inside another class:
#The above can be acheived in two ways:
#1.Composition 2.Inheritance

#Composition (Has-a relationship)

class Engine:
	a=10
	def __init__(self):
		self.b=20
	
	def m1(self):
		print("Engine Specific Functionality")

class Car:
	def __init__(self):
		self.engine=Engine()
		
	def m2(self):
		print("Car Uses Engine specific functionality")
		print(self.engine.a)
		print(self.engine.b)
		self.engine.m1()

c=Car()
c.m2()		

