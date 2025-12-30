import json

fobj=open("product.json","w")
products=[]

while True:
    prod_name=input("Enter product name: ")
    price=float(input("Enter product price: "))
    prod={'prod_name':prod_name,'price':price}
    products.append(prod)
    ans=input("Add another product?  ")
    if ans=="no":
        break
json.dump(products,fobj)
fobj.close()
