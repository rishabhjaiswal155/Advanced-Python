#__str__(self) method

class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
		
	def __str__(self):
		return "This is Student with Name:{} and Marks:{}".format(self.name,self.marks)

s1=Student('Rishabh',92)
s2=Student('Vishal',89)
print(s1)
print(s2)		