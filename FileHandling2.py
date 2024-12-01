#Reading character data from the file
#using read()
f=open('Rishi.txt','r')
data=f.read() #read() reads total data from the file
print("Reading total data completes....")
print(data)
f.close()

#using read(n)
f=open('Rishi.txt','r')
char=f.read(10) #To read n charcters of data from file
print("Reading only 10 number of characters completes....")
print(char)
f.close()

#using readline()
f=open('Rishi.txt','r')
line=f.readline() #To read only one line of data from file
print("Reading only 1 line of data completes....")
print(line)
f.close()


