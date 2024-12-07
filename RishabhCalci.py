#static method(It does not consist of any instance or static variable)
#It contains only local variable 

class RishabhCalci:
	@staticmethod #Declaring static method with local variable x and y
	def add(x,y):
		print("Sum of two numbers:",x+y)
	
	@staticmethod #Declaring static method with local variable x and y
	def mul(x,y):
		print("Product of two numbers:",x*y)
		
	@staticmethod #Declaring static method with local variable x and y
	def div(x,y):
		print("Division of two numbers:",x/y)
		
	@staticmethod #Declaring static method with local variable x and y
	def sub(x,y):
		print("substraction of two numbers:",x-y)
		
	@staticmethod #Declaring static method with local variable x and y
	def average(x,y):
		print("The Average of two numbers:",(x+y)/2)
		
RishabhCalci.add(15,6) #calling static method using class name
RishabhCalci.mul(18,6)
RishabhCalci.div(21,7)
RishabhCalci.sub(15,6)
RishabhCalci.average(15,6)