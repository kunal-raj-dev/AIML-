# Design & create an online store for Products (name, price).

# Track total products being created.

# Create a static method to calculate discount on each product based on a % parameter.

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products created = {cls.count}")
    

    @staticmethod
    def calcDiscount(price, discount):
        print(f"Price after discount = { price - (price * (discount/100))}")
    

prod1 = Product("soap" , 100)
prod1.get_info()
prod1.calcDiscount(100, 20)

prod2 = Product("towel" , 200)
prod1.get_info()
prod1.calcDiscount(200, 17)

Product.get_count()