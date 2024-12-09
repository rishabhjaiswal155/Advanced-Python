#Multi Level Inheritance

class Parent:
	def m1(self):
		print("Parent class Method m1()")
		
class Child(Parent):
	def m2(self):
		print("Child class method m2()")
		
class SubChild(Child):
	def m3(self):
		print("SubChild class Method m3()")
		
sc=SubChild()
sc.m1()
sc.m2()
sc.m3()
