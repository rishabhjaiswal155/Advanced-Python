#Hybrid Inheritance

class Parent1:
	def m1(self):
		print("Parent1 class method m1()")
		
class Parent2:
	def m1(self):
		print("Parent2 class method m1()")
		
class Child(Parent1,Parent2):
	def m2(self):
		print("Child class Method m2()")
		
class SubChild1(Child):
	def m3(self):
		print("SubChild1 class method m3()")
		
class SubChild2(Child):
	def m4(self):
		print("SubChild2 class method m4()")
		
print(SubChild1.mro())
print(SubChild2.mro())
print(Child.mro())
print(Parent1.mro())
print(Parent2.mro())
