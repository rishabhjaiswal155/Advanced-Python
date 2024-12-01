#Logging

import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p') #if filename is not specified default log messages will print on console
#default filemode='a' append we can change it to 'w' to overwrite
#format keyword argument to format the log messages
#To format timestamp in log messages format='%(asctime)s'
#To change date and time format datefmt='%d/%m/%Y %I or %H:%M:%S %p'

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
	