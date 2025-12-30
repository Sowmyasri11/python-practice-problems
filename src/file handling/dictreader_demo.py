import csv

fobj=open("product.csv","r")
drobj=csv.DictReader(fobj)
for row in drobj:
    print(row)

fobj.close()
