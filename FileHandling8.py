#Handling csv files using csv module
#Writting employee data into csv file

import csv
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f) #returns the writer object pointing to f
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input("Enter the number of Employees:"))
    for i in range(n):
        eno=int(input("Enter Employee Number:"))
        ename=input("Enter Employee Name:")
        esal=float(input("Enter Employee Salary:"))
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Total Employee Data inserted into csv file:",f.name)

