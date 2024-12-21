#Python program to insert mutiple employee data into employees table
import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='root123',database='python')
    cursor=con.cursor()
    query="insert into employees values(%s,%s,%s,%s)"
    records=[(3000,'Amol',5698.0,'Amravati'),(4000,'Shreyash',9876.00,'Buldhana'),(5000,'Surabhi',8975.00,'Khamgaon')]
    cursor.executemany(query,records)
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