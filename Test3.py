#static variable:
#Static variable can be accessed uisng classname and object reference variable also.
class Test3:
	a=100 #static variable
	def __init__(self):
		self.b=200 #instance variable
t1=Test3()
t1.a=3000 #instance variable for t1
t1.b=4000 #Modifying instance varaible
t2=Test3()
print(t1.a,t1.b) #3000 4000 here t1.a is accessing instance variable
print(t2.a,t2.b) #100 200 Here t2.a is accessing static variable
print(Test3.a,t1.b) #100 4000 Here Test3.a is accessing static variable using classname		