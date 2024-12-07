#instance methods 
class Student3:
	def __init__(self,name,marks):
		self.name=name #instance variables
		self.marks=marks
		self.display() #another instance method is called inside instance method using self.
	
	def display(self): #instance method
		print("Student name:",self.name)
		print("Student marks:",self.marks)
		self.grade() #another instance method is called inside instance method using self.
	
	def grade(self): #instance method
		if self.marks>=70:
			print("You got A grade")
		elif self.marks>=55 and self.marks<70:
			print("You got B grade")
		elif self.marks>=40 and self.marks<55:
			print("You got C grade")
		else:
			print("You failed,please try next time")

s=Student3("Rishabh",92)
s1=Student3("Lucky",25)

			