#Python Program to Delete the data in mysql database employees table
import pymysql
try:
	con=pymysql.connect(host='localhost',user='root',password='root123',database='Python')
	cursor=con.cursor()
	salrange=float(input("Enter Employees Salary range for which Employee data is to be deleted:"))
	query="delete from employees where esal>%s"
	cursor.execute(query %salrange)
	con.commit()
	print("Deletion of Employees Data Successfull.")
except pymysql.DatabaseError as m:
	if con!=None:
		con.rollback()
		print("There is a problem:",m)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
	