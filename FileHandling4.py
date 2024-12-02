f=open('Rishi.txt','w')
data='Python is very interesting language to learn..'
f.write(data)
print(data)
f.close()
with open('Rishi.txt','r+') as f:
    text=f.read()
    print("Reading of Data completes....")
    print(text)
    print("printing of Data to console completes....")
    print("The Current position of cursor is:",f.tell()) #tell() returns the current position of cursor
    f.seek(15) #seek() used to seek the cursor to particular position
    f.write("boring!!!!!")
    print("Modification of data completes...")
    f.seek(0)
    text=f.read()
    print("Reading of Modified Data completes....")
    print(text)
    print("Printing of Modified Data to console completes....")
   
    
    