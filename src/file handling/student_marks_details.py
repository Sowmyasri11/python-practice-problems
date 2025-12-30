try:
    fobj=open("marks.txt","a")

    while True:
        roll_no=int(input("Enter roll no: "))
        name=input("Enter name: ")
        subject1=int(input("Enter subject 1: "))
        subject2=int(input("Enter subject 2: "))
        print(roll_no,name,subject1,subject2,file=fobj,flush=True)
        ans=input("Do you want to add another student? ")
        if ans=="no":
            break
except OSError:
    print("Oops! cannot create file.")
finally:
    fobj.close()

