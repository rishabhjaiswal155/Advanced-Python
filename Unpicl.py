import Employee,pickle
with open('Employee.dat','rb') as f:
	print("Employee Data after Unnpickling:")
	while True:
		try:
			obj=pickle.load(f)
			obj.display()
		except EOFError:
			print("UnPickling of all Employee Completes.....")
			break
		