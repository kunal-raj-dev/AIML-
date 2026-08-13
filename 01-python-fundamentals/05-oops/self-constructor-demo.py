# Understanding the 'self' parameter in Python OOPs
# 'self' represents the instance of the class and binds the attributes with the given arguments.

class Car:
    def __init__(self, brand, model, price):
        # self.attribute_name binds to this particular object instance
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        # Accessing instance variables via self
        print(f"Car: {self.brand} {self.model} | Price: ₹{self.price:,}")

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
        print(f"Discount of {percent}% applied! New price: ₹{self.price:,}")


# Creating objects
car1 = Car("Tata", "Nexon", 950000)
car2 = Car("Mahindra", "XUV700", 1600000)

car1.display_details()
car1.apply_discount(10)

car2.display_details()
