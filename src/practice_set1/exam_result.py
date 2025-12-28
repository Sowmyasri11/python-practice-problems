marks=list(map(int,input("Enter the marks :").split()))

failed = False
for m in marks:
    if m < 35:
        failed = True
        break

if failed:
    print("FAIL")
else:
    average = sum(marks) / 5
    if average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")