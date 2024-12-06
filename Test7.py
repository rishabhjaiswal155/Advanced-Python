#Local Variable and example

class Test7:
	a=100 #static variable
	def __init__(self):
		self.a=200 #instance variable
		Test7.a=300 #Modifying static variable
		a=400 #Local variable
		print(a)
	def m1(self):
		self.a=400 #instance variable
		print(self.a) #accessing instance variable
		print(Test7.a) #Accessing static variable
	@classmethod
	def m2(cls):
		cls.a=500 #Creating instance variable
		Test7.a=600 #Modifying static variable
print(Test7.a)
t1=Test7()
print(t1.a,Test7.a)
t1.m1()
t1.a=700
t1.m2()
t2=Test7()
t2.m2()	
		