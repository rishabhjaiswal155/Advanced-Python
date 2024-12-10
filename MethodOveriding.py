#Method Overiding

class Parent:
	def property(self):
		print("Land|Cash|Power|Gold")
	
	def marriage(self):
		print("Arranged Marriage..")
		
class Child(Parent):
	def marriage(self):
		super().marriage()
		print("Love Marriage...")
		
c=Child()
c.property()
c.marriage()
