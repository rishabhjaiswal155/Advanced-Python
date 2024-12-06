#Modifying static variable
class Test6:
	a=10 #static variable
	def __init__(self):
		Test6.a=20 #Modifying static variable inside the constructor using classname
	def m1(self):
		Test6.a=30 #Modifying static variable inside the instance method using classname
	@classmethod
	def m2(cls):
		Test6.a=40 #Modifying static variable inside the class method using classname
		cls.a=50 #Modifying static variable inside the class method using cls variable
	@staticmethod
	def m3():
		Test6.a=60 #Modifying static variable inside the static method using classname
print(Test6.a)
t1=Test6()
print(t1.a)
print(Test6.a)
Test6.a=70 #Modifying static variable outside the class using classname
print(Test6.a)
t1.m1()
print(Test6.a)
t1.m2()
print(Test6.a)
t1.m3()
print(Test6.a)


