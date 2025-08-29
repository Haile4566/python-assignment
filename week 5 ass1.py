# Assignment 1: Design Your Own Class

# Parent class
class Device:
    def init(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"Device: {self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def init(self, brand, model, os, storage):
        super().init(brand, model)   # Call parent constructor
        self.os = os
        self.storage = storage
    
    def info(self):
        return f"Smartphone: {self.brand} {self.model}, OS: {self.os}, Storage: {self.storage}GB"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
phone2 = Smartphone("Apple", "iPhone 14", "iOS", 128)

print(phone1.info())
print(phone2.info())