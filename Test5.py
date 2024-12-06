#Accessing static variables:

class Test5:
	a=10 #static variable
	def __init__(self):
		print(self.a) #Accessing static variable from inside the constructor using self variable
		print(Test5.a)#Accessing static variable from inside the constructor using classname.
	def m1(self):
		print(self.a) #Accessing static variable from inside the instance method using self variable
		print(Test5.a)#Accessing static variable from inside the instance method using classname
	@classmethod
	def m2(cls):
		print(cls.a) #Accessing static variable from inside the class method using cls variable
		print(Test5.a) #Accessing static variable from inside the class method using classname
	@staticmethod
	def m3():
		print(Test5.a) #Accessing static variable from inside the static method using classname
t=Test5()
print(t.a) #Accessing static variable from outside the class using object reference variable
print(Test5.a)#Accessing static variable from outside the class using classname
t.m1()
t.m2()
t.m3()
		