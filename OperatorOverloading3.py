#Operator Overloading Example

class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	
	def __mul__(self,other):
		return self.salary*other.days
		
class Timesheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days
		
	def __mul__(self,other):
		return self.days*other.salary
	
e=Employee('Rishabh',2000)
t=Timesheet('Rishabh',22)
print("The Total Monthly salary:",e*t)
print("The Total Monthly salary:",t*e)