import csv
fobj = None
try:
    fobj = open("emp.csv","w",newline='')
    wobj = csv.writer(fobj)
    wobj.writerow(["emp_no","ename","salary"])
    while True:
        emp_no = input("Enter emp_no: ")
        ename = input("Enter ename: ")
        salary = input("Enter salary: ")
        wobj.writerow([emp_no,ename,salary])
        ans=input("Add another employee?")
        if ans=='no':
            break
except:
    print("Something went wrong")
finally:
    if fobj is not None:
        fobj.close()


