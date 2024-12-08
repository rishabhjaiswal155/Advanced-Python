#Calling Parent class Constructor from child class constructor using super()

class A:
	a=10
	def __init__(self):
		print("parent class Constructor....")
		self.b=20
		
	def m1(self):
		self.c=30
		
class B(A):
	def __init__(self):
		print("Child class Constructor....")
		self.d=40
		super().__init__() #Calling Parent class Constructor inside Child Class using super().
		
	def m2(self):
		self.e=50
		
b=B()
b.m1()
b.m2()
print(b.a,b.b,b.c,b.d,b.e)