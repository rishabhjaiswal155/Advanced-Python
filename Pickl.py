import Employee,pickle
n=int(input('Enter the number of Employees:'))
with open('Employee.dat','wb') as f:
	for i in range(n):
		eno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee name:")
		esal=float(input("Enter Employee salary:"))
		eaddr=input("Enter Employee address:")
		e=Employee.Employee(eno,ename,esal,eaddr)
		pickle.dump(e,f)
	print("Pickling of Employee's data completes")

	