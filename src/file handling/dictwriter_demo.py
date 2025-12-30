import csv
try:
    fobj=open("product.csv","w",newline='')
    dwobj=csv.DictWriter(fobj,fieldnames=["id","pname","price"])
    dwobj.writeheader()
    while True:
        product_id=int(input("enter product id"))
        product_name=input("enter product name")
        price=int(input("enter price"))
        dwobj.writerow({'id':product_id,'pname':product_name,'price':price})
        ans=input("add another product ")
        if ans=='no':
            break
except:
    print("Unable to write data.")
finally:

    if fobj is not None:
        fobj.close()
