#Ways to handle Method Overloading requirements in Python:
#1.using default arguments
#2.using Variable length arguments

#1.using default arguments
class Test15:
	def sum(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			print("The sum of Three numbers:",a+b+c)
		
		elif a!=None and b!=None:
			print("The sum of two numbers:",a+b)
			
		elif a!=None:
			print("The Sum:",a)
		
		else:
			print("Please Provide at least one argument!!")
			
t=Test15()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)

#2.using Variable length argument

class Test16:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print("sum=",total)

t1=Test16()
t1.sum()
t1.sum(10)
t1.sum(10,20)
t1.sum(10,20,30)

#having simlar number of argument but of different type:
class Test17:
    def m1(self,a):
        self.a=a
        print(self.a)
t=Test17()
t.m1(10)
t.m1(10.45)
t.m1('Rishabh')
