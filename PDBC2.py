#Python program to create a employees table in mysql database.
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
cursor=con.cursor()
query='create table employees(eno int(4) primary key,ename varchar(10),esal double(10,2),eaddr varchar(20))'
cursor.execute(query)
print("Table is created...")		
cursor.close()
con.close()