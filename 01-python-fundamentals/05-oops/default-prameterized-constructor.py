class Laptop:
    

    def __init__(self, brand, RAM, storage, storage_type):
        self.brand = brand
        self.RAM = RAM
        self.storage = storage
        self.storage_type = storage_type

    def info(self):
        return self.RAM , self.storage

prod1 = Laptop("hp", 16 , 512, "ssd")
ram,storage = prod1.info()

print(f"Ram : {ram}\nStorage : {storage}GB")

