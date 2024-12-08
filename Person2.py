#Example using both Inheritance and Composition

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def eatAndDrink(self):
		print("Eat Food and Drink Water...")
		
class Employee(Person): #IS-A relatioship
	def __init__(self,name,age,eno,esal,car):
		super().__init__(name,age)
		self.eno=eno
		self.esal=esal
		self.car=car #Has-A Relationship
		
	
	def work(self):
		print("Codes in Python....")
		
	def empInfo(self):
		print("Employee Name:",self.name)
		print("Employee Age:",self.age)
		print("Employee Number:",self.eno)
		print("Employee Salary:",self.esal)
		print("Car Information:")
		self.car.carInfo()
	

class Car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
		
	def carInfo(self):
		print("\tCar Name:",self.name)
		print("\tCar Model:",self.model)
		print("\tCar Color:",self.color)
		
	
car=Car("Grand Vitara","Zeta","White")
e=Employee("Rishabh",28,102,52000,car)
e.empInfo()
e.eatAndDrink()
e.work()
