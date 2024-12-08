#2.Inheritance(Is-A relationship)

class P: #parent class
	a=10
	def __init__(self):
		print("Constructor....")
		self.b=20
	
	def m1(self):
		print("Instance method....")
		self.c=30
		
	@classmethod
	def m2(cls):
		print("class method...")
		cls.d=40
	
	@staticmethod
	def m3():
		print("static method....")
		e=50
	
class C(P): #Child Class
	pass
	
c=C() #Creating object of child class
c.m1() #Accessing members
c.m2()
c.m3()
print(c.a,c.b,c.c,c.d) #variable e cannot be accessed as it is local variable of m3()
