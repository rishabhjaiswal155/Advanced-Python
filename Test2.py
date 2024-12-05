#Accessing and deleting instance variable

class Test2:
	def __init__(self):
		self.a=100
		self.b=200
		self.c=300
		self.d=400
	def m1(self):
		print("a=",self.a) #Accessing instance variable within the class using self variable
		print("b=",self.b)
		self.a=900
		self.b=1000
		del self.c #Deleting instance variable inside the class using del keyword
t=Test2()
print("a=",t.a) #Accessing instance variable outside the class using object reference variable
print("b=",t.b)
print("c=",t.c)
print(t.__dict__)
t.m1()
print("a=",t.a)
print("b=",t.b)
print(t.__dict__)
del t.d #Deleting instance variable outside the class using object reference variable with del keyword
print(t.__dict__)
