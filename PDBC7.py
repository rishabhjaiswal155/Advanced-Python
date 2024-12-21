#Python Program to Update the data in mysql database employees table
import pymysql
try:
	con=pymysql.connect(host='localhost',user='root',password='root123',database='Python')
	cursor=con.cursor()
	incrementsal=float(input("Enter incremented Salary amount:"))
	salrange=float(input("Enter Employees Salary range for which salary is to be incremented:"))
	query="update employees set esal=esal+%s where esal<%s"
	cursor.execute(query %(incrementsal,salrange))
	con.commit()
	print("Updation of Employees salary Successfull.")
except pymysql.DatabaseError as m:
	if con!=None:
		con.rollback()
		print("There is a problem:",m)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
	