#Instance Variables
#Declaring instance variables

class Test1:
	def __init__(self):
		self.a=100 #Declaring instance variable inside constructor
	def m1(self):
		self.b=200 #Declaring instance variable inside instance method
        
t=Test1()
print(t.__dict__) #This property returns the key value pair of all instance variables declare.
t.m1()
print(t.__dict__)
t.c=300 #Declaring instance variable outside the class using object reference variable
print(t.__dict__)
