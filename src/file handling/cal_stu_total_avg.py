fobj=None
try:
    fobj=open('marks.txt','r')
    while True:
        stud=fobj.readline()
        if stud=='':
            break
        roll_no,name,subj1,subj2=stud.split()
        total=int(subj1)+int(subj2)
        avg=total/2
        result="PASS" if int(subj1)>=40 and int(subj2)>=40 else "FAIL"
        print(f'{roll_no}\t {name}\t {avg}\t {result}')
except OSError:
    print("Unable to read data")
finally:
    if fobj is not None:
        fobj.close()


