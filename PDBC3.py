#Python program to drop a employees table in mysql database.
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
cursor=con.cursor()
query='drop table employees'
cursor.execute(query)
print("Table is dropped...")
cursor.close()
con.close()
		
