try:
    fobj = open("file1.txt", "w")
    fobj.write("python ")
    fobj.write("java ")
    fobj.write(""" python
    is easy programming language""")
except OSError:
    print("unable to create file")
except TypeError:
    print("values must be string type")
finally:
    fobj.close()
