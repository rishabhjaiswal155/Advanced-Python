#we can use static variable of Parent class from child class using super()
#But we cannot use instance variable of Parent class from child class using super() directly

class Parent:
	a=10
	def __init__(self):
		self.b=20
	
	def m1(self):
		print("Instance method of parent class")
		
	@classmethod
	def m2(cls):
		print("Class Method of Parent class")
		
	@staticmethod
	def m3():
		print("static Method of parent class")
		
class Child(Parent):
    a=888
    def __init__(self):
        self.b=99
        print(self.b)
        super().__init__()
        print(super().a)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()
        
c=Child()

