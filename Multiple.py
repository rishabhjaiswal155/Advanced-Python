#Multiple Inheritance

class Parent1:
	def m1(self):
		print("Parent1 class method m1()")
		
class Parent2:
	def m1(self): #Here Both Parents have same method name m1()
		print("Parent2 class method m1()")
		
class Child(Parent1,Parent2): #Which parent's method executes depends on the order,Here Parent1's m1 executes
	def m2(self):
		print("Child class method m2()")
		
c=Child()
c.m1() #Here Parent1's m1() method executes
c.m2()