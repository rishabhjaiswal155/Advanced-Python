#Python program to insert mutiple employee data taken from keyboard into employees table
import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
    cursor=con.cursor()
    eno=int(input("Enter Employee number:"))
    ename=input("Enter Employee Name:")
    esal=float(input("Enter Employee Salary:"))
    eaddr=input("Enter Employee Address:")
    query="insert into employees values(%s,'%s',%s,'%s')"
    cursor.execute(query %(eno,ename,esal,eaddr))
    con.commit()
    print("Multiple Employees data inserted successfully...")
except pymysql.DatabaseError as m:
    if con!=None:
        con.rollback()
        print("There is a problem:",m)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()