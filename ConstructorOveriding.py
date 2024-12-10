#Constructor overiding

class Parent:
	def __init__(self):
		print("Zero argument Constructor...")
		
class Child(Parent):
	def __init__(self,a):
		print("one Argument Constructor....")

#c=Child() #These gives error as only most recent one is executes only..
c1=Child(10)