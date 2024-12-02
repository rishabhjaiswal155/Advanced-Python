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

#Reading employee data from csv file nd print it to console

import csv
with open('emp.csv','r',newline='') as f:
    r=csv.reader(f) #returns the reader object pointing to f
    data=list(r)
    print("Reading data from csv file",f.name)
    for line in data:
        for word in line:
            print(word,'\t',end='')
        print()

