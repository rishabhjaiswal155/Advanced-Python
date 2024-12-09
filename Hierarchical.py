#Hierarchical Inheritance

class Parent:
	def m1(self):
		print("Parent1 class method m1()")
		
class Child1(Parent):
	def m2(self):
		print("Child1 class method m2()")
		
class Child2(Parent): 
	def m3(self):
		print("Child2 class method m3()")
		
c1=Child1()
c1.m1() 
c1.m2()
c2=Child2()
c2.m1()
c2.m3()