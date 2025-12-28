salary = int(input("Enter your salary: "))
late_days = int(input("Enter your late days: "))
absent_days = int(input("Enter your absent days: "))

final_salary = salary

if late_days > 10:
    final_salary -= salary * 0.10
elif late_days > 5:
    final_salary -= salary * 0.05


if absent_days > 2:
    final_salary -= salary * 0.05

print(int(final_salary))