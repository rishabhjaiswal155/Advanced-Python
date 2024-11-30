#Userdefined Exception or Custom Exception

class TooYoungException(Exception):
	def __init__(self,arg):
		self.msg=arg

class TooOldException(Exception):
	def __init__(self,arg):
		self.msg=arg

age=int(input("Enter Your age for Driving licence:"))
if age<18:
	raise TooYoungException("You are under age for driving license,please wait to turn 18 years old!!!")
elif age>65:
	raise TooOldException("You are overage to apply for driving licence!!!")
else:
	print("Your appplication has been registered successfully!!!")
