#Nested methods:

class Test11:
	def m1(self):
		print("Outer method:")
		
		def calci(a,b):
			print("The Sum of two numbers:",a+b)
			print("The Product of two numbers:",a*b)
			print("The Division of two numbers:",a/b)
			print("The Difference of two numbers:",a-b)
			
		calci(10,5)
		calci(158,54)
		calci(245,65)
		
t=Test11()
t.m1()