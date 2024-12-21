#Python Program to connect with mySql Database and print its Version
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root123',database='Python')
if con!=None:
	print("Connection established Successfully!!!")
else:
	print("Connection establishment failed..")


