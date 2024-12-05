#Program to define a Student class and create the mutiple objects of it.
class Student2:
	def __init__(self,name,rollno,age,marks): #Here self is python provided implict variable pointing to the current object.
		self.name=name #using self we can access object variables(instance variables) and object methods(instance methods) of current object.
		self.rollno=rollno
		self.age=age
		self.marks=marks
		print(id(self))
	def talk(self):
		print("My name is:",self.name)
		print("My rollno is:",self.rollno)
		print("My age is:",self.age)
		print("My marks is:",self.marks)
s1=Student2('Rishabh',100,28,95)
s2=Student2('Vishal',101,25,85)
print(id(s1))
print(s1.name,s1.marks)
print(s2.name,s2.marks)
s1.talk()
s2.talk()
