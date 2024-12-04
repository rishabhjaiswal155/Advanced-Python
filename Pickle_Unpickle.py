#Pickling and unPickling

import pickle
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
with open('emp.dat','wb') as f:
	e=Employee(100,'Rishabh',52000,'Akola')
	pickle.dump(e,f)
	print("Pickling of Employee Data completes....")
with open('emp.dat','rb') as f:
    obj=pickle.load(f)
    obj.display()
    print("Unpickling of Employee Data from emp.dat completes....")