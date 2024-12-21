#Python Program to insert the data into employees table.
import pymysql
try:
	con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
	cursor=con.cursor()
	query="insert into employees values(2000,'vishal',4500.0,'Kaij')"
	cursor.execute(query)
	con.commit()
	print("Data inserted successfully!!!")
except pymysql.DatabaseError as m:
	if con!=None:
		con.rollback()
		print('There is a problem:',m)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
		