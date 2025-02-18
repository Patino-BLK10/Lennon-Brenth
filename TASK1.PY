class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
car1 = Car("Skygo", "Vios", 2022)
car2 = Car("Rusi", "Montero", 2025)
car1.display_info()
print("")  
car2.display_info()


