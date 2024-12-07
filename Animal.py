#Class method
class Animal:
	legs=4
	@classmethod
	def walk(cls,name):
		print("{} walks with {} legs".format(name,cls.legs))
a=Animal()
a.walk('Dog')		
a.walk('Cat')		