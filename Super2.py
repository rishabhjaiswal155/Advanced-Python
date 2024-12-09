#calling method of particular class using super() in case of multi level Inheritance

class A:
	def m1(self):
		print("m1() method of class A")
		

class B(A):
	def m1(self):
		print("m1() method of class B")
		

class C(B):
	def m1(self):
		print("m1() method of class C")
		

class D(C):
	def m1(self):
		print("m1() method of class D")
		

class E(D):
	def m1(self):
		B.m1(self) #one way to call method of particular class without using super() in case of multi level inheritance
		super(C,self).m1() #second way to call method of particular class with using super() in case of multi level inheritance	

e=E()
e.m1()