#Types of Inheritance:

#Single Level Inheritance

class Parent:
	def m1(self):
		print("Parent class method m1()")
	
class Child(Parent):
	def m2(self):
		print("Child class method m2()")

c=Child()
c.m1()
c.m2()