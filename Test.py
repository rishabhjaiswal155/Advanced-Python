#Constructor

class Test:
	def __init__(self):
		print("No argument constuctor")
	def __init__(self,x):
		print("one argument constructor")
	def __init__(self,x,y):
		print("Two argument constructor")
#t1=Test() #These gives error as recent constructor is having two arguments as Constructor Overloading is not possible in python
#t2=Test(10) #These gives error as recent constructor is having two arguments as Constructor Overloading is not possible in python
t3=Test(10,20)
#t1.__init__()
#t2.__init__(10)
t3.__init__(10,20) #These call __init__() as method call


		