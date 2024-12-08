#passing members of one class to another class

class Employee1:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
	
	def display(self):
		print("Employee number :",self.eno)
		print("Employee name :",self.ename)
		print("Employee Salary :",self.esal)
		
class Test:
	def modify(emp): #static method
		emp.esal=emp.esal+10000 #esal member of Employee class passing to Test class
		emp.display() #display member of one class is called in another class

e=Employee1(100,"Rishabh",25000)
Test.modify(e) #member of one class is passed to another class

		