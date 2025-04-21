from datetime import datetime
from typing import Any
# Base class
class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @property
    def age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.year

    def description(self) -> str:
        return f"{self.make} {self.model}, Year: {self.year}, Age: {self.age} years"


# a car is a vehicle + fuel_type, take a look at the main function to check
# how the class should be initialized and what the description should return
class Car:
    pass


if __name__ == "__main__":
    # Create a Vehicle instance
    vehicle = Vehicle(make="Scott", model="Spark", year=2015)
    assert vehicle.description() == "Scott Spark, Year: 2015, Age: 10 years"

    # Create a Car instance
    tesla = Car(make="Tesla", model="Model S", year=2020, fuel_type="Electric")
    clio = Car("Diesel", "Renault", "Clio", 2018)
    assert tesla.description() == "Tesla Model S, Year: 2020, Age: 5 years, Fuel Type: Electric"
    assert clio.description() == "Renault Clio, Year: 2018, Age: 7 years, Fuel Type: Diesel"
