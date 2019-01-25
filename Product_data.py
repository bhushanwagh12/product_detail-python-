class Product:
    shopping_mall_name=" Relaince Mall "
    shopping_mall_address=" Khadki pune "
    def __init__(self,pid,pname,pprice,pbrand):
        self.product_id=pid
        self.product_name=pname
        self.product_price=pprice
        self.product_brand=pbrand
    def infoo(self):
        print("shopping_mall_name= ",Product.shopping_mall_name)
        print("shopping_mall_address =",Product.shopping_mall_address)
    def info(self):
        print("*"*40)
        print(" Product_ID = ",self.product_id)
        print(" Product_name = ",self.product_name)
        print(" Product_Price = ",self.product_price)
        print(" Product_brand = ",self.product_brand)
        print("*"*40)
p=Product(10,"Noodles",48,"Maggie")
p.info()
p.infoo()
p1=Product(20,"Shampoo",20,"Dove")
p1.info()
p=Product(10,"Biscuits",48,"Good Day")
p.info()
p=Product(10,"Water",48,"Bisleri")
p.info()
p=Product(10,"Shirts",48,"Linen")
p.info()
p=Product(10,"Trousers",48,"BABA")
p.info()
p=Product(10,"Washing powder",48,"Rin")
p.info()
