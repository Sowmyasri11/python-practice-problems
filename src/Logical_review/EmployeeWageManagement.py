


def get_employee_data():
    try:
        employee_id = int(input("Enter employee ID: "))
        employee_name = input("Enter employee name: ")
        salary_per_hour = int(input("Enter salary per hour: "))

        print("Enter daily working hours for 7 days: ")
        daily_hours=[]
        for day in range(1,8):
            hours=float(input(f"Day {day}:"))
            if hours <= 0:
                raise ValueError("Working hours cannot be negative")
            daily_hours.append(hours)

        return{
            "id":employee_id,
            "name":employee_name,
            "salary_per_hour":salary_per_hour,
            "daily_hours":daily_hours
            }
    except ValueError as e:
        print("Invalid input:", e)
        return None

def calculate_wage(employee):

    total_hours=sum(employee["daily_hours"])
    salary_per_hour=employee["salary_per_hour"]

    daily_wages=[hours *salary_per_hour for hours in employee["daily_hours"]]

    weekly_wage=sum(daily_wages)

    if total_hours>40:
        bonus=0.10*weekly_wage
        weekly_wage+=bonus
    else:
        bonus=0
    return weekly_wage,daily_wages,bonus

def save_to_file(employee,weekly_wage,bonus):

    with open("employee_records.txt","a") as file:
        file.write(f"Employee ID: {employee['id']}\n")
        file.write(f"Employee Name: {employee['name']}\n")
        file.write(f"Employee Salary: {employee['salary_per_hour']}\n")
        file.write(f"Employee Weekly wage: {employee['weekly_wage']}\n")
        file.write(f"Bonus Applied : {employee['bonus']}\n")
        file.write("-" *30+"\n")

if __name__=="__main__":
    employees=[]
    highest_earner=None
    highest_wage=0

    while True:
        employee=get_employee_data()
        if employees is None:
            continue

        weekly_wage,daily_wages,bonus=calculate_wage(employee)
        employee["weekly_wage"]=weekly_wage

        employees.append(employee)

        save_to_file(employee,weekly_wage,bonus)

        if weekly_wage>highest_wage:
            highest_wage=weekly_wage
            highest_earner=employee["name"]

        choice=input("Would you like to save the employee records? (yes/no): ")
        if choice!="yes":
            break
    print("Highest wage:", highest_wage)
    print("Highest earner:", highest_earner)



