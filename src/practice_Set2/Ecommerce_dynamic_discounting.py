from unicodedata import category


def apply_discount(products):

    return{
        product_name:{
            **product_info,
            'price':(
                product_info['price']*0.85
                if product_info['category'] == 'Electronics' and
                product_info['price']>50
                else product_info['price'] * 0.90
                if product_info['category'] == 'Fashion' and product_info['price'] > 50
                else product_info['price']

            )
        }
        for product_name,product_info in products.items()
    }

def get_products():
    products={}
    num_of_products=int(input("Enter number of products: "))

    for _ in range(num_of_products):
        product_name=input("Enter product name: ")
        price=int(input("Enter product price: "))
        category=input("Enter product category: ")
        products[product_name]={'price': price, 'category': category}

    return products

products=get_products()
discounted_products=apply_discount(products)

print(discounted_products)


