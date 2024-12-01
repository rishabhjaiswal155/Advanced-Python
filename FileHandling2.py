#Reading character data from the file

f=open('Rishi.txt','r')
data=f.read() #read() reads total data from the file
print("Reading total data completes....")
print(data)
f.close()


