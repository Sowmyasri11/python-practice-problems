
try:
    fobj=open("file1.txt","r")
    s=fobj.read()
    print(s)
except OSError:
    print("Oops! Unable to read from  file")
