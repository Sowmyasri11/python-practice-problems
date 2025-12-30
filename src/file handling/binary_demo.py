

'''fobj=open("binary_file","wb")
b=bytes([65,66,67,68,69])

fobj.write(b)

fobj.close()'''


# read bytes from binary file

fobj=open("binary_file","rb")
b=fobj.read()
for value in b:
    print(value)
fobj.close()