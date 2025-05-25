# Parent class
class Vehicle: 
    def __init__(self,name,capacity): 
        self.name = name 
        self.capacity = capacity 

    def __str__(self): 
        return f"{self.name} with capacity {self.capacity}"

# Child class 
class Bus(Vehicle):
    def __init__(self,name,capacity, fare_per_person):
        super()>__init__(name,capacity)
        self.fare_per_person = fare_per_person 

    def calculate_total_fare(self): 
        return self.capacity * self.fare_per_person 
