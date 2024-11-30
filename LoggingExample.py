#Logging Example
import logging
logging.basicConfig(filename="log.txt",level=logging.INFO)
try:
	logging.info("A new Request comes....")
	x=int(input("Enter number1:"))
	y=int(input("Enter number2:"))
	print("The Division of two numbers is:",x/y)
except ZeroDivisionError as msg:
	print("The Denominator should not be Zero")
	logging.exception(msg)
except ValueError as msg:
	print("The numbers should be int value")
	logging.exception(msg)
logging.info("The request processing completes....")
	