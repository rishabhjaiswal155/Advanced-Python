#Python program to fetch the employee data from mysql database and print on the console
import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
    cursor=con.cursor()
    query="select * from employees"
    cursor.execute(query)
    data=cursor.fetchall()
    for d in data:
        print("Employee Number:",d[0])
        print("Employee Name:",d[1])
        print("Employee Salary:",d[2])
        print("Employee Address:",d[3])
        print()
    print("Employee Data Fetched SuccessFully.")
except pymysql.DatabaseError as m:
    if con!=None:
        con.rollback()
        print("There is a problem:",m)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        