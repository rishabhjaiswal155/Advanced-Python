#Handling the binary data in file

f1=open('image1.jpg','rb')
f2=open('newImage1.jpg','wb')
databytes=f1.read()
print("Reading of Binary file completes...")
f2.write(databytes)
print("writing of Binary file completes...")

