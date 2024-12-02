#Program to take fileName from keyboard as input,check whether file exists or not,if exists print its content
import os
fname=input("Enter the name of file:")
with open(fname,'r') as f:
	if os.path.isfile(fname):
		print("File exists:",fname)
		content=f.read()
		print("Reading the content of file completes...")
		print(content)
		print("Printing the content of file to console completes...")
	else:
		print("File:",fname,"doesn't exists")
		
		
