#File Handling in Python
#file modes like r(read),w(write),a(append),r+(read then write),w+(write then read),a+(append then read),x(Exclusive creation mode for write operation)
#various file properties like name,closed,readable(),writeable() etc
#Inbuilt functions to open a file is open()
#Inbuilt functions to close a file is close()

f=open('Rishi.txt','w')
print("name of the file:",f.name)
print("is the file writable:",f.writable())
print("is the file readable:",f.readable())
print("is the file closed:",f.closed)
f.close()
print("is the file closed:",f.closed)





