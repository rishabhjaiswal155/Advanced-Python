#Composition Example Employee has a car

class Car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
		
	def carInfo(self):
		print("Car Name:",self.name)
		print("Car Model:",self.model)
		print("Car's color:",self.color)
		
class Employee:
	def __init__(self,eno,ename,car):
		self.eno=eno
		self.ename=ename
		self.car=car
	
	def empInfo(self):
		print("Employee number:",self.eno)
		print("Employee name:",self.ename)
		print("Employee's car information:")
		self.car.carInfo()
		
c=Car("Grand Vitara","Zeta","White")
e=Employee(102,"Rishabh",c)
e.empInfo()