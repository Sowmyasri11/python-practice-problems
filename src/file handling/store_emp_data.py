import json

fobj=open("employees.json","w")
emp_id=int(input("Enter employee id: "))
emp_name=str(input("Enter employee name: "))

salary=int(input("Enter employee salary: "))

json.dump({'EmployeeNo':emp_id,'EmployeeName': emp_name,'Salary':salary},fobj)
fobj.close()