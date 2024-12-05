#Declaring static variables

class Test4:
	a=10 #Declaring static variables inside the class
	def __init__(self):
		Test4.b=20 #Declaring static variables inside the constructor using classname
	def m1(self):
		Test4.c=30 #Declaring static variables inside the instance method using classname
	@classmethod #Decorator for declaring classmethod
	def m2(cls):
		Test4.d=40 #Declaring static variables inside the class method using classname
		cls.e=50  #Declaring static variables inside the class method using cls variable
	@staticmethod #Decorator for declaring staticmethod
	def m3():
		Test4.f=60 #Declaring static variables inside the static method using classname
Test4.g=70 #Declaring static variable outside the class using classname
Test4.a=100 #Modifying the static variable using classname,we can access the static variable using object reference but we cannot modify it using object reference
print(Test4.__dict__)
print()
t1=Test4()
print(Test4.__dict__)
print()
t1.m1()
print(Test4.__dict__)
print()
t1.m2()
print(Test4.__dict__)
print()
Test4.m2()
print(Test4.__dict__)
print()
t1.m3()
print(Test4.__dict__)
print()
Test4.m3()
print(Test4.__dict__)
print()
