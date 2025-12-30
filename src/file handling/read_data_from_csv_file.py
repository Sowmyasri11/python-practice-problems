import csv
fobj=None
robj=None
try:
    fobj=open("emp.csv","r")
    robj=csv.reader(fobj)


    for row in robj:
        print(row)
except:
    print("Unable to read data")
finally:
    if fobj is not None:
        fobj.close()

