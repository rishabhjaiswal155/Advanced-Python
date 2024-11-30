#Nested try except finally
try:
	print("Outer try block")
	#print(10/0)
	try:
		print("Inner try block")
		#print(10/0)
	except:
		print("Exception caused and handle in inner except block")
	finally:
		print("inner finally block")
except:
	print("Exception caused and handle in Outer except block")
finally:
	print("Outer finally block")

#try-except-else-finally
try:
	print("try block")
	#print(10/0)
except:
	print("except block handles the exception caused in try block")
else:
	print("else block executes only when no exception caused in try block")
finally:
	print("finally block exeutes always whether execption handle or not handle")
