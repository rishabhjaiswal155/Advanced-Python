#Python Program to connect with mySql Database.
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root123',database='Python')
if con!=None:
	print("Connection established Successfully!!!")
else:
	print("Connection establishment failed..")
con.close()

