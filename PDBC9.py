#Python program to fetch the employee data from mysql database and print on the console
import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
    cursor=con.cursor()
    query="select * from employees"
    cursor.execute(query)
    data=cursor.fetchone()
    print("Employee Number:",data[0])
    print("Employee Name",data[1])
    print("Employee Salary:",data[2])
    print("Employee Address:",data[3])
    print("Employee Data Fetched Successfully.")
except pymysql.DatabaseError as m:
    if con!=None:
        con.rollback()
        print("There is a problem:",m)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        