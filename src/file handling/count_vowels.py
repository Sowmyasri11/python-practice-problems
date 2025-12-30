count = 0
fobj = None

try:
    fobj = open("file1.txt", "r")
    while True:
        ch = fobj.read(1)
        if ch == "":
            break
        if ch in "aeiouAEIOU":
            count += 1
    print(f"Count of vowels: {count}")

except OSError:
    print("Unable to read data")

finally:
    if fobj is not None:
        fobj.close()
