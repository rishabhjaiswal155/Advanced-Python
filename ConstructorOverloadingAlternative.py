#Constructor Overloading: It is not available in Python
#using default arguments and variable length argument we can handle the requirement for Constructor overloading

class Test18:
	def __init__(self,a=None,b=None,c=None):
		print("with 0 or 1 or 2 or 3 argument constructor...")
		
t=Test18()
t1=Test18(10)
t2=Test18(10,20)
t3=Test18(10,20,30)

class Test19:
	def __init__(self,*a):
		print("with 0 or 1..... constructor arguments")
t=Test19()
t1=Test19(10)
t2=Test19(10,20)
t3=Test19(10,20,0,40,50,60)

