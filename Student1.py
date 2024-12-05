#Creation of class and Object

class Student1: #defining class having class name as Student1
	def __init__(self): #constructor definition
		self.name="Rishabh" #instance variables
		self.rollno=100
		self.age=28
		self.marks=92
	def talk(self): #instance method definition
		print("My name is:",self.name)
		print("My roll number is:",self.rollno)
		print("My Age is:",self.age)
		print("My marks are:",self.marks)
s1=Student1() #Here s1 is refernce variable pointing to object of class Student1
print(s1.name)
print(s1.marks)
s1.talk()

		
		