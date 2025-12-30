fobj1 = None
fobj2 = None

try:
    fobj1=open("file1.txt","r")
    fobj2=open("file2.txt","w")
    data=fobj1.read()
    fobj2.write(data)
    print("file copied...")
except OSError :
    print("error in creating copy")

finally:
    if fobj1 is not None:
        fobj1.close()
    #fobj1.close()
    if fobj2 is not None:
        fobj2.close()
