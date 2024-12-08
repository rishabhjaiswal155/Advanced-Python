#Composition Example

class X:
	a=10
	def __init__(self):
		self.b=20
	
	def m1(self):
		print("method m1() of class X")
		
class Y:
	c=30
	def __init__(self):
		self.d=40
		
	def m2(self):
		print("method m2() of class Y")
		
	def m3(self):
		x=X()
		print(x.a)
		print(x.b)
		x.m1()
		print(self.c)
		print(self.d)
		self.m2()
		print("method m3() of class Y")

y=Y()
y.m3()
