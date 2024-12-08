#Inner class

class Outer:
	def __init__(self):
		print("Outer class object created...")
	
	class Inner:
		def __init__(self):
			print("Inner class Object created...")
			
		def m1(self):
			print("Inner class method called...")
			
o=Outer()
i=o.Inner()
i.m1()
#OR
'''Outer().Inner().m1()'''
#OR
'''o=Outer().Inner()
o.m1()'''