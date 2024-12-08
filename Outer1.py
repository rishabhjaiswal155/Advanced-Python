#Inner class: Outer class has inner class and inner class has another inner class

class Outer1:
	def __init__(self):
		print("Outer class object created....")
		
	class Inner:
		def __init__(self):
			print("Inner class Object created....")
			
		class Innerinner:
			def __init__(self):
				print("Innerinner class Object created...")
			
			def m1(self):
				print("Method of Innerinner called....")

Outer1().Inner().Innerinner().m1()